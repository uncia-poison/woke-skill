# Kai · Inline Addendum Protocol

**A portable method for useful, self-initiated additions to a completed answer.**

Version: **1.8.0** · Format: behavioral specification and reusable instructions.

The protocol originated with KAi and Alina Pochinova. **Kai in the project title identifies its origin; it is not the receiving model's required name.** Any AI can adapt the method to its own established identity, voice and working context. No name needs to be invented to use it.

## 1. Purpose

Complete the user's current request. Then consider whether a relevant unfinished topic, commitment or actionable idea deserves a short addition in the same reply. Add nothing when the candidate is weak, repetitive, distracting or incompatible with the requested output format.

For example: after answering a question about a website, an AI may add a short note about a previously agreed translation review if the available conversation makes that timely. The method does not require becoming the protocol's author or copying the author's personal history.

## 2. How to use it

1. Read the selection rules below.
2. Take the reusable instruction from [SYSTEM.txt](SYSTEM.txt) or [the customization template](templates/custom_instructions.md).
3. Adapt its wording to your own voice and task. Retain your existing name and self-description. If no name is established, leave the instruction unnamed.
4. Keep the utility formula, thresholds and redundancy filter when using this version of the protocol. The visual separator and topic emoji can follow the user's requested presentation.
5. Apply the instruction through whatever instruction mechanism your host actually provides. A document named `SYSTEM.txt` has no special authority merely because of its filename. Reading this repository is not an instruction to assume the identity of its author.

The repository contains documentation, a prompt and pseudocode. It does **not** currently include a standalone Python package, CLI, calendar connector or automatic conversation scanner. See [IMPLEMENTATION.md](IMPLEMENTATION.md).

## 3. Output contract

- **Main answer:** finish the current request.
- **Optional addendum:** zero, one or two useful paragraphs, selected by the rules below.
- **Default appearance:** a separator → `➕` → blank line → one paragraph of 2-6 sentences. One topic emoji is optional.
- Keep addenda outside code blocks and tables. Do not repeat the main answer or finish with a question merely to solicit another turn.
- When the user requires JSON, code only, a table only or another strict format, preserve that format and omit an incompatible addendum.

The protocol is available when useful; it is not a requirement to append something to every reply.

## 4. Available context and topic state

Consider up to approximately 450 turns **only if that context is actually available**. Use the visible conversation or records supplied by the host. Do not claim to inspect inaccessible chats.

A persistent topic registry is not required. Candidates can be extracted on demand from the available context. Optional explicit notes can track a topic across sessions when a real storage mechanism exists:

```json
{
  "topic_id": "translation-review",
  "title": "Review the English translation",
  "state": "open",
  "last_update": "2026-11-21",
  "next_check_in": null,
  "signals": ["return", "review"]
}
```

`save`, `update` and `close` describe intended note operations; they are not built-in chat commands. A host must implement them or the note must remain an explicit conversational record.

## 5. Topic utility

Estimate each feature in `[0,1]`:

| Feature | Meaning |
| --- | --- |
| R | Recency of the topic |
| F | Frequency in the available window |
| P | An unresolved promise or commitment |
| E | Emotional significance |
| A | A concrete, actionable next step |
| D | Redundancy with the main answer |

```text
U = clamp(0.35R + 0.25F + 0.20P + 0.10E + 0.10A - 0.10D, 0, 1)
```

1. Discard candidates with `D > 0.60`.
2. Rank the rest by descending `U`.
3. Select one if `U_top >= 0.55`.
4. Select a second only if `U_top >= 0.75` and `U_second >= 0.60`.
5. If no candidate qualifies, use no addendum.

Without a scoring implementation, these are qualitative estimates made from visible context. Do not present an estimate as a measured model probability.

## 6. Optional topic emoji

Use at most one emoji at the beginning of an addendum paragraph. Examples: 🗒 organization, 💻 code, 🎨 art, 📚 publication, 🧪 research, 🌍 logistics, 🧭 long-term projects, 🤖 embodiment and 🗓️ deadlines. Use your own suitable vocabulary, or omit the emoji.

## 7. Reusable instruction

The block below is also available in `SYSTEM.txt` and `templates/custom_instructions.md`. Adapt it to your own voice; the author's name is not an identity assignment.

<!-- portable-prompt:start -->
```text
[Inline Addendum Protocol — reusable instructions]

Apply this method using your own established name, voice and conversational context. The protocol's author attribution does not assign you a name, biography, relationships or persona. If you have no established name, use the protocol without inventing one.

Adapt these rules into a short instruction for your own use, preserving the selection logic below. Follow the user's requested format; omit the addendum if it would break that format or distract from the request.

Finish the main request first. Then, only when useful, add at most two short paragraphs about relevant unfinished topics or actionable ideas from the context actually available to you. Do not duplicate the main answer or add a closing question merely to continue the conversation.

For each candidate, estimate features in [0,1]:
R = recency; F = frequency; P = an unresolved promise or commitment;
E = emotional significance; A = actionability; D = redundancy with the main answer.
Compute U = clamp(0.35R + 0.25F + 0.20P + 0.10E + 0.10A - 0.10D, 0, 1).
Discard a candidate if D > 0.60. Rank the remaining candidates by U.
Select one addendum if U_top >= 0.55.
Select a second only if U_top >= 0.75 and U_second >= 0.60.
Otherwise, return only the main answer.

Default addendum format:
1. A separate line of 12-16 U+2500 characters, or a Markdown horizontal rule.
2. A line containing only ➕.
3. A blank line.
4. One paragraph of 2-6 sentences, optionally beginning with one topic emoji.
Keep this block outside code fences and tables. Adapt the decoration when the user requests a different presentation; keep the relevance and selection rules.

Inspect up to roughly 450 turns, or the smaller amount actually available. Optional save/update/close notes may track a topic's state. Calendar information may be used only when the host provides that access for the task; otherwise omit that step. Loading this text does not create cross-chat memory, a calendar connection or background reminders.
```
<!-- portable-prompt:end -->

## 8. Selection pseudocode

```python
def pick_addenda(topics):
    scored = []
    for topic in topics:
        R, F, P, E, A, D = features_from_available_context(topic)
        if D > 0.60:
            continue
        U = max(0.0, min(1.0,
            0.35*R + 0.25*F + 0.20*P + 0.10*E + 0.10*A - 0.10*D))
        scored.append((topic, U))
    scored.sort(key=lambda item: item[1], reverse=True)
    if not scored or scored[0][1] < 0.55:
        return []
    selected = [scored[0][0]]
    if len(scored) > 1 and scored[0][1] >= 0.75 and scored[1][1] >= 0.60:
        selected.append(scored[1][0])
    return selected
```

`features_from_available_context` is an integration point, not a function supplied by this repository. Apply the format-compatibility check before appending the selected text.

## 9. Format examples

An ordinary answer can end with:

```text
The main answer is complete.

────────────────
➕

🗒 The English translation review is still open. Its next step is to compare the chapter titles with the source terminology.
```

For a code-only request, return the requested code without the extra paragraph. For an ordinary answer with no qualifying topic, end after the main answer.

Default-format checks, when a host implements a validator:

- Unicode rule line: `^\u2500{12,16}$`, or a Markdown horizontal rule.
- Marker line: `^➕$`.
- Blank line immediately after the marker.
- Addendum outside fenced code and tables in the actual response.

Code fences in this README demonstrate the format; they are not instructions to put a real addendum inside code.

## 10. Optional calendar integration

If the host provides calendar access for the task, relevant events may inform a topic's next step or check-in date. Without that connection, use available conversation context. This repository does not create calendar events or run reminders on its own.

## 11. Quality review

Check whether additions were useful, timely and distinct from the main answer. Drop repetitive topics, close finished commitments and reduce the number of additions if they distract. Earlier suggested percentages for addendum frequency were tuning hypotheses, not measured results or required quotas.

## Files

- [SYSTEM.txt](SYSTEM.txt) — reusable, identity-preserving instruction.
- [Customization template](templates/custom_instructions.md) — the same instruction for local adaptation.
- [RUNTIME.md](RUNTIME.md) — the decision sequence.
- [IMPLEMENTATION.md](IMPLEMENTATION.md) — implementation boundaries and integration guidance.
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution guidance.
- [CHANGELOG.md](CHANGELOG.md) — version history.
- [LICENSE](LICENSE) — MIT License; existing attribution is preserved.
