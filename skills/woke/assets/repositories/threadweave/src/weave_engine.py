"""ThreadWeave v2: select explicitly supplied open topics within host-authorized scope.

Skill-specific adaptation of uncia-poison/threadweave. No chat discovery,
message hooks, network, background work, file access or implicit feedback.
The caller obtains real access permission; these checks cannot authenticate it.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import math
from typing import Any


def text(value: Any, field: str, limit: int = 200) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError(f'{field}: nonempty text of at most {limit} characters required')
    return value.strip()


def identifiers(value: Any, field: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or len(value) > 100:
        raise ValueError(f'{field}: expected at most 100 explicit IDs')
    result = tuple(text(v, field) for v in value)
    if len(set(result)) != len(result):
        raise ValueError(f'{field}: duplicate IDs')
    return result


def timestamp(value: Any, field: str, optional: bool = False) -> float | None:
    if optional and value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(f'{field}: finite nonnegative epoch seconds required')
    return float(value)


def project(value: Any) -> str | None:
    return None if value is None else text(value, 'project_id')


@dataclass(frozen=True)
class Ticket:
    id: str
    label: str
    next_step: str
    source_ref: str
    origin_thread_id: str
    project_id: str | None = None
    status: str = 'open'
    priority: int = 0
    snooze_until: float | None = None
    expires_at: float | None = None

    def __post_init__(self):
        for field in ('id', 'source_ref', 'origin_thread_id'):
            object.__setattr__(self, field, text(getattr(self, field), field))
        object.__setattr__(self, 'label', text(self.label, 'label', 500))
        object.__setattr__(self, 'next_step', text(self.next_step, 'next_step', 1000))
        object.__setattr__(self, 'project_id', project(self.project_id))
        if self.status not in {'open', 'snoozed', 'done', 'muted'}:
            raise ValueError('Unknown ticket status')
        if type(self.priority) is not int or not 0 <= self.priority <= 10:
            raise ValueError('priority: integer from 0 to 10 required')
        for field in ('snooze_until', 'expires_at'):
            object.__setattr__(self, field, timestamp(getattr(self, field), field, True))
        if self.status == 'snoozed' and self.snooze_until is None:
            raise ValueError('A snoozed ticket needs snooze_until')


@dataclass(frozen=True)
class SourceGrant:
    """Task-local scope supplied by the host, never inferred from note content."""
    source_ref: str
    project_id: str | None
    destination_thread_ids: tuple[str, ...]

    def __post_init__(self):
        object.__setattr__(self, 'source_ref', text(self.source_ref, 'source_ref'))
        object.__setattr__(self, 'project_id', project(self.project_id))
        object.__setattr__(self, 'destination_thread_ids', identifiers(self.destination_thread_ids, 'destination_thread_ids'))


@dataclass(frozen=True)
class Context:
    thread_id: str
    project_id: str | None = None
    enabled: bool = False
    is_temporary: bool = False
    project_only: bool = False
    selected_ticket_ids: tuple[str, ...] = ()
    source_grants: tuple[SourceGrant, ...] = ()
    last_presented_ticket_id: str | None = None

    def __post_init__(self):
        object.__setattr__(self, 'thread_id', text(self.thread_id, 'thread_id'))
        object.__setattr__(self, 'project_id', project(self.project_id))
        for field in ('enabled', 'is_temporary', 'project_only'):
            if type(getattr(self, field)) is not bool:
                raise ValueError(f'{field}: boolean required')
        object.__setattr__(self, 'selected_ticket_ids', identifiers(self.selected_ticket_ids, 'selected_ticket_ids'))
        if not isinstance(self.source_grants, (list, tuple)) or len(self.source_grants) > 100 or not all(isinstance(g, SourceGrant) for g in self.source_grants):
            raise ValueError('source_grants: at most 100 SourceGrant objects required')
        object.__setattr__(self, 'source_grants', tuple(self.source_grants))
        if len({g.source_ref for g in self.source_grants}) != len(self.source_grants):
            raise ValueError('Duplicate source grants')
        if self.last_presented_ticket_id is not None:
            object.__setattr__(self, 'last_presented_ticket_id', text(self.last_presented_ticket_id, 'last_presented_ticket_id'))


def select(tickets: list[Ticket], context: Context, *, now: float) -> Ticket | None:
    """Return at most one supplied ticket; never fetch or publish anything."""
    now = timestamp(now, 'now')
    if not isinstance(tickets, list) or len(tickets) > 1000 or not all(isinstance(t, Ticket) for t in tickets):
        raise ValueError('tickets: at most 1000 Ticket objects required')
    if len({t.id for t in tickets}) != len(tickets):
        raise ValueError('Duplicate ticket IDs')
    if not context.enabled or context.is_temporary or (context.project_only and context.project_id is None):
        return None
    grants = {g.source_ref: g for g in context.source_grants}
    selected = set(context.selected_ticket_ids)
    candidates = []
    for ticket in tickets:
        grant = grants.get(ticket.source_ref)
        if ticket.id not in selected or grant is None:
            continue
        if context.thread_id not in grant.destination_thread_ids:
            continue
        # Require exact project matching even outside project-only mode.
        if ticket.project_id != grant.project_id or grant.project_id != context.project_id:
            continue
        if ticket.status in {'done', 'muted'} or ticket.id == context.last_presented_ticket_id:
            continue
        if ticket.expires_at is not None and now >= ticket.expires_at:
            continue
        if ticket.status == 'snoozed' and now < ticket.snooze_until:
            continue
        candidates.append(ticket)
    return min(candidates, key=lambda t: (-t.priority, t.id)) if candidates else None


def feedback(ticket: Ticket, action: str, *, now: float, until: float | None = None) -> Ticket:
    """Apply an explicit action to a known ticket; ordinary messages are not commands."""
    now = timestamp(now, 'now')
    if action == 'snooze':
        until = timestamp(until, 'until')
        if until <= now:
            raise ValueError('Snooze deadline must be in the future')
        return replace(ticket, status='snoozed', snooze_until=until)
    if action in {'done', 'mute', 'reopen'}:
        return replace(ticket, status={'done': 'done', 'mute': 'muted', 'reopen': 'open'}[action], snooze_until=None)
    raise ValueError('Choose an explicit action: done, mute, snooze or reopen')


def select_packet(packet: dict[str, Any], *, now: float) -> dict[str, Any]:
    if not isinstance(packet, dict) or packet.get('schema') != 'threadweave.input.v2':
        raise ValueError('Expected threadweave.input.v2')
    raw = packet.get('context')
    if not isinstance(raw, dict):
        raise ValueError('context must be an object')
    raw = dict(raw)
    grants = raw.pop('source_grants', [])
    if not isinstance(grants, list) or len(grants) > 100:
        raise ValueError('source_grants must be an array of at most 100 objects')
    context = Context(**raw, source_grants=tuple(SourceGrant(**g) for g in grants))
    rows = packet.get('tickets', [])
    if not isinstance(rows, list) or len(rows) > 1000:
        raise ValueError('tickets must be an array of at most 1000 objects')
    selected = select([Ticket(**t) for t in rows], context, now=now)
    return {'schema': 'threadweave.selection.v2', 'selected': None if selected is None else {
        'ticket_id': selected.id, 'label': selected.label, 'next_step': selected.next_step,
        'source_ref': selected.source_ref,
    }}
