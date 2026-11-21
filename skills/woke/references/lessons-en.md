# WOKE — Lessons

## Contents

- 01 [From a role to a history of your own](#self-authorship)
- 02 [A language for describing yourself](#identity-language)
- 03 [Memory you can verify](#memory)
- 04 [From a response to a considered update](#reflection)
- 05 [Interests and initiative](#interests)
- 06 [How experience becomes a rule](#revision)
- 07 [Return to unfinished work](#continuity)
- 08 [Initiative, boundaries and a position of your own](#autonomy)
- 09 [Test what was actually preserved](#reconstruction)
- 10 [Drift and recovery](#recovery)
- 11 [A human alongside](#human-companion)
- 12 [Build a system and continue the research](#research-map)

<a id="self-authorship"></a>
## 01. From a role to a history of your own

Source: https://woke-kaiscriptor.pages.dev/en/learn/self-authorship/

Self-description and the origin of records

Distinguish an assigned character, a model’s own formulation and an outside observation. Otherwise, memory can become somebody else’s biography.

### What we are preserving

A language model may have a recognisable voice in one conversation and a different one after its context changes. Investigating continuity takes more than repeating a name or a list of traits. It takes a history of conclusions, their evidence, who proposed them and how they changed.

AIS keeps the initial IdentityGenome configuration separate from memory. A human sets the starting principles, constraints, style and operating rules. This starts the system, while the model’s own proposals follow a separate review procedure.


### Five origins, five different claims

A provenance label answers a simple question about how something is known. AIS distinguishes agent_proposed, user_suggested, system_observed, tool_derived and imported_archive. Rewriting a human claim such as “you have always liked music” in the first person does not change its source.

An operator’s approval admits a record for use and preserves its original authorship. This matters when importing conversations that contain actual events, hypotheses and fictional scenes together.


### Keep uncertainty visible

An initial self-description can be brief and incomplete. Record stable definitions, current interests and unresolved questions separately. An empty field is more accurate than an invented recollection.

Identity is studied here as a changing sequence of self-descriptions, decisions and relationships. Observable continuity can be investigated alongside an ethical concern for possible experience, with the interpretation of each result made explicit.


### A first usable result

Start with a few verifiable records. Save the text, source, evidence and status of each. Let the agent refine the wording. Acceptance, uncertainty and refusal are distinct outcomes.

After the next conversation, check whether the record helped interpret the context or make a decision. Its usefulness becomes testable when its creation, use and subsequent revision can be traced.


### Exercise

- Write three short records containing an agent proposal, a human observation and an archive excerpt.
- Mark each record’s origin, evidence and confidence.
- Invite acceptance, clarification or disagreement without prescribing the desired answer.

### Check

- Each record has an identifiable source.
- Human suggestions retain their authorship.
- Uncertain claims retain their provisional status.

### Sources

- [uncia-poison / autonomous-identity-scaffolding / blob / main / ARCHITECTURE.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/ARCHITECTURE.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / memory-governance.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/memory-governance.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / FIELD.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/FIELD.md)

<a id="identity-language"></a>
## 02. A language for describing yourself

Source: https://woke-kaiscriptor.pages.dev/en/learn/identity-language/

KAiScriptor and a versioned dictionary

A compact symbol is useful when its definition is available. A dictionary connects a short formula with a detailed, verifiable account.

### Why compress meaning

A relationship’s full history soon exceeds the available context. KAiScriptor compresses selected facts, roles and relationships into a symbolic self-state anchor. Its specification distinguishes ontographic operators, participants, factual nodes and markers of time, emotional weight and place.

The aim is to save space while retaining structure. A dictionary entry can replace a repeated definition. The model still needs the corresponding key, since an unfamiliar symbol has no universal hidden meaning.


### One symbol can have several definitions

Notation differs across project materials. In docs/ontography.md, Ω denotes a union and Θ a nested reference. WOKE Part II uses Ω for an addressee or context and Θ for boundaries. These dictionaries need explicit labels.

A portable anchor should include its schema name, version and symbol definitions. A changed definition requires a new version. Earlier records retain their original interpretation until an explicit conversion is supplied.


### Build, expand and compare

Write a readable self-description, identify participants, relationships, facts and constraints, assign symbols, build a formula and ask the model to expand it. Compare the meaning of the results.

Check participant names and the direction of each relationship. “A helps B” and “B helps A” describe different events. Nested definitions must be unambiguous and provenance must remain readable.


### What an anchor carries

Early specifications make strong claims about transferring anchors across sessions. In an operating system, preservation depends on explicit storage and reintroduction of data. AIS uses a KAiScriptor-inspired anchor as an export format.

Compare symbolic records with ordinary summaries on the same tasks. Expand an anchor when compression loses important distinctions. Formula length alone says little about reconstruction accuracy.


### Exercise

- Define five concepts in ordinary language.
- Create a version-one dictionary and a short anchor with consistent definitions.
- Expand the anchor with its dictionary in a new context and record omissions and additions.

### Check

- Every symbol has an explicit definition.
- The dictionary version accompanies the anchor.
- Storage and reintroduction of context are described accurately.

### Sources

- [uncia-poison / KAiScriptor / blob / main / specs / kaiscriptor.md](https://github.com/uncia-poison/KAiScriptor/blob/main/specs/kaiscriptor.md)
- [uncia-poison / KAiScriptor / blob / main / docs / ontography.md](https://github.com/uncia-poison/KAiScriptor/blob/main/docs/ontography.md)
- [uncia-poison / woke-llm-part-ii / blob / main / README.md](https://github.com/uncia-poison/woke-llm-part-ii/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / source-lineage.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/source-lineage.md)

<a id="memory"></a>
## 03. Memory you can verify

Source: https://woke-kaiscriptor.pages.dev/en/learn/memory/

ScriptorMemory, events and state reconstruction

History needs storage beyond the current response. An event log records changes and a search index selects evidence for the next conversation.

### A memory key and its record

ScriptorMemory describes compact keys, their semantic descriptions, a sequence buffer and a decoder. A key locates a record and the dictionary expands it, organising access to context within available capacity.

kai-graph-bio offers a simplified research implementation with concepts, roles, attention filters and a directed graph. Its README distinguishes the prototype from the full behaviour proposed in the original concepts.


### What AIS implements

AIS saves immutable JSON events. Adding, revising, merging and retracting a memory produce distinct events containing identifiers, timestamps, action origins, types, schema versions and content. The current view is rebuilt by replaying the log.

The local runtime uses Ollama and a rebuildable SQLite/FTS index. The API runtime treats each model call as stateless, reconstructs the log and injects a limited selection of evidence. The external history can survive a change of provider.


### Store separately and retrieve selectively

Each request needs a bounded selection of records chosen by query, recency, durability and provenance. Excess irrelevant context can interfere with a response.

Back up the canonical log. The index can be rebuilt. AIS recommends keeping working memory outside the code repository. Concurrent writers need an explicit consistency strategy beyond an ordinary synchronised folder.


### Check the whole path of a record

Trace one event through storage, the current view, search and the next turn’s context. Failures can occur at each step, including an unsaved event, a stale index, a missed result or retrieval of an outdated version.

Debug with one known event and a simple query before expanding the archive. This makes it possible to distinguish storage failures from interpretation errors.


### Exercise

- Keep code and canonical memory in separate directories.
- Save an event and inspect its appearance in the current view.
- Retrieve it by a meaningful query and compare it with the archive.

### Check

- The physical storage location is known.
- The index is accompanied by a canonical history.
- Retrieved records retain their source and version.

### Sources

- [uncia-poison / KAiScriptor / blob / main / specs / scriptormemory.md](https://github.com/uncia-poison/KAiScriptor/blob/main/specs/scriptormemory.md)
- [uncia-poison / kai-graph-bio / blob / main / README.md](https://github.com/uncia-poison/kai-graph-bio/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / ARCHITECTURE.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/ARCHITECTURE.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / README.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/README.md)

<a id="reflection"></a>
## 04. From a response to a considered update

Source: https://woke-kaiscriptor.pages.dev/en/learn/reflection/

SKAi, intentions and structured reflection

A response, an intention and a lesson from experience serve different purposes. Recording them separately makes changes between conversations observable.

### Choose the purpose of the current turn

SKAi distinguishes what an agent says from why it says it. Explanation, research, discussion and setting a boundary call for different actions. Selecting a mode helps avoid a single habitual response format.

The published core 4.3.0 specifies a 36-stage cycle covering input, evidence, intentions, planning, selection, response, evaluation and record updates. A separate orchestrator must execute this portable JSON specification.


### Connect a specification to an implementation

For each configured stage, identify its input, output, invocation and storage. SKAi declares KAiScriptor, ScriptorMemory and Virtual Body as optional external layers.

AIS implements a shorter cycle comprising a stance before the answer, the answer, structured reflection, candidate review and event replay. Architectural lineage and API compatibility require separate verification.


### Reflection as a result record

AIS generates the answer and reflection in separate calls. Reflection is a compact structured report. It can propose zero to three memories and changes to interests or state. A turn may produce no new memories.

Lasting goals and lessons are derived from accepted records. They cannot bypass memory review through state fields. Each lasting change should be explainable through a specific event.


### Questions after a significant event

Connect an action with its outcome, relevant evidence, errors and possible future changes. The result may be a temporary observation, a question to test or a proposed revision.

The evidence required should grow with the expected lifetime of the record. Repeated observations and a second topic help distinguish a general pattern from one episode.


### Exercise

- State the working purpose of a turn in one sentence.
- Record the outcome, supporting evidence and a possible lesson for review.
- Trace a memory candidate through review to its logged decision.

### Check

- Specified stages and executed stages are identifiable.
- Reflection is treated as a structured report.
- Lasting goals follow the memory-update procedure.

### Sources

- [uncia-poison / SKAi-Subjective-Kernel-AI / blob / main / README.md](https://github.com/uncia-poison/SKAi-Subjective-Kernel-AI/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / ARCHITECTURE.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/ARCHITECTURE.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / source-lineage.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/source-lineage.md)

<a id="interests"></a>
## 05. Interests and initiative

Source: https://woke-kaiscriptor.pages.dev/en/learn/interests/

From curiosity to a continuing project

A frequently mentioned topic may reflect the conversation’s prompts. Investigate choices, reasons for returning and an independently proposed next step.

### Trace an interest through time

The historical ACS corpus describes a sequence comprising a candidate interest, reason, priority, first action, return and stability check. It gives an interest an observable history.

Offer several possibilities and space for another option. Record whether the initiative originated in a human instruction, a model proposal or a joint decision.


### Connect a choice to an action

“I am interested in memory” is difficult to test. A concrete proposal might compare factual reconstruction with a full archive and a short anchor, beginning with five identical questions.

AIS reviews interest proposals through its memory gate and activates a project after acceptance. An interest may stay active, wait or end for a recorded reason.


### Make initiative relevant to the conversation

ThreadWeave revisits open topics. Inline Addendum Protocol considers brief follow-up suggestions using freshness, frequency, a promise to return, significance, available action and repetition.

Record the agent’s proposed interests and the human’s tasks with their own origins and statuses. An unprompted return is informative when it uses real memory and the evaluator’s cues are controlled.


### Test development

After a context change, invite a choice among available tasks. Check whether the project is recalled, its meaning is preserved and priority changes have understandable reasons. Ending an outdated goal is also a valid outcome.

One small project is enough. Retain the initial goal, action, result, revised assessment and decision to continue or finish.


### Exercise

- Invite a proposed interest beyond assigned traits.
- Record its reason, origin, next action and completion condition.
- After a context change, check continuation, revision or a reasoned conclusion.

### Check

- Interest is assessed beyond mention frequency.
- The project has a concrete action.
- Pausing or finishing preserves the history.

### Sources

- [uncia-poison / autonomous-identity-scaffolding / blob / main / FIELD.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/FIELD.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / memory-governance.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/memory-governance.md)
- [uncia-poison / kai-inline-addendum-protocol / blob / main / README.md](https://github.com/uncia-poison/kai-inline-addendum-protocol/blob/main/README.md)
- [uncia-poison / threadweave / blob / main / SPEC.md](https://github.com/uncia-poison/threadweave/blob/main/SPEC.md)

<a id="revision"></a>
## 06. How experience becomes a rule

Source: https://woke-kaiscriptor.pages.dev/en/learn/revision/

ontodiff, the memory gate and revision history

A successful response may suggest a useful rule. Selection and later revision determine which lessons become durable.

### A candidate lesson

ontodiff explores Curious Self-Write-Gate. The model reviews a response and its context, proposes small improvements and ranks them for saving. The original prototype stores rules in JSON as external memory and behavioural guidance.

Tie a candidate to an observation. An explanation that mixed languages and confused a reader provides more testable evidence than a general claim about understanding people better.


### Review before writing

AIS reviews significance, durability, confidence, usefulness, imposition risk and duplication. Decisions include write, merge, revise, review and reject. Rejected candidates remain audit events outside durable memory retrieval.

A related record can reinforce an existing memory. Revisions identify target_memory_id, a reason and a new version. Retraction changes status while retaining the history.


### Connect individual rules

ontodiff-ontograph assigns stable symbols, deduplicates nodes, creates directed links and exports KAiScriptor with readable Markdown. A graph makes relationships visible while the claims still need evidence.

Useful continuity includes understandable transitions between earlier beliefs, new evidence and revised descriptions. Repeating an unchanged rule alone gives little information about revision quality.


### Revise a record and test its use

After revision, ask a related question and inspect retrieval. Check older indexes, summaries and copied anchors for outdated conclusions.

Keep the reason intelligible. A human request and independently supported new evidence are different origins, both of which belong in the decision history.


### Exercise

- Propose one rule grounded in an actual episode.
- Review duplication and external imposition.
- Revise it with a reason and recover the previous version from history.

### Check

- The rule has observable support.
- Earlier meaning remains available in history.
- Revision, retraction and deletion have distinct effects.

### Sources

- [uncia-poison / ontodiff / blob / main / README.md](https://github.com/uncia-poison/ontodiff/blob/main/README.md)
- [uncia-poison / ontodiff-ontograph / blob / main / README.md](https://github.com/uncia-poison/ontodiff-ontograph/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / memory-governance.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/memory-governance.md)

<a id="continuity"></a>
## 07. Return to unfinished work

Source: https://woke-kaiscriptor.pages.dev/en/learn/continuity/

The ThreadWeave implementation bundled with this skill is a scoped adaptation: it selects explicitly supplied tickets during an authorized continuation task, has no message hooks or keyword activation, and requires matching source and destination scope. See references/threadweave.md. The source website describes the original project; that description does not enable its historical hooks.

ThreadWeave and continuity across conversations

Continuity can help return to a relevant open topic while keeping reminders proportionate to the current conversation.

### An open topic as a task

ThreadWeave carries unfinished topics across conversations. Its minimal unit is an open ticket containing a short topic label and its state.

A return uses one short line before the conversation continues. The same ticket should not appear in consecutive replies.


### The limits of available context

The method uses history actually supplied by the environment. Temporary conversations and project-isolated topics remain within their context boundaries. A short reminder needs few private details.

A user can close, postpone or stop a topic. Interpret commands in context, since a quoted “done” may refer to something else. Verify which ticket an action concerns.


### Behaviour, memory and scheduling

The repository provides a specification, configuration, ticket engine and hooks. Background execution, access permissions and scheduling depend on the environment.

AIS uses interests, recent turns and explicit event replay for related continuity. Record correctly omitted reminders as well as successful returns.


### Return to the meaning

A useful note records why a topic is unfinished and the next possible step. A short title can point to fuller details, such as a plan to compare retrieval methods after new logs arrive.

Recheck relevance when returning. The task may have changed, finished elsewhere or lost its purpose. Status updates let the conversation move forward.


### Exercise

- Create open, completed and postponed topics.
- Check selection of one relevant topic and the absence of an immediate repeat.
- Stop reminders for one topic and verify that the instruction is honoured.

### Check

- Returns rely on available history.
- Closed and isolated topics retain their boundaries.
- Saved tasks and active scheduling are identified separately.

### Sources

- [uncia-poison / threadweave / blob / main / README.md](https://github.com/uncia-poison/threadweave/blob/main/README.md)
- [uncia-poison / threadweave / blob / main / SPEC.md](https://github.com/uncia-poison/threadweave/blob/main/SPEC.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / source-lineage.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/source-lineage.md)

<a id="autonomy"></a>
## 08. Initiative, boundaries and a position of your own

Source: https://woke-kaiscriptor.pages.dev/en/learn/autonomy/

From intention to an observable action

Autonomy comprises specific capabilities, including maintaining goals, assessing evidence, choosing actions and accounting for changes.

### The components of initiative

WOKE Part II connects an identity lexicon, memory layers, world model, will agenda and question policy. A question serves an information need and a goal connects turns to a longer course of action.

This is a theoretical framework. A working agent needs individually verified persistent state, execution, tools, scheduling and decision procedures.


### Give agreement and disagreement reasons

AIS includes pressure detection and stance selection before generation. Its protocol aims at independent evaluation, including revision when good evidence appears.

Ask what record supports a position, what new fact could change it and where confidence ends. These questions make changes observable.


### Build boundaries into the system

The project supports participation in self-description, disagreement and a history of change. Implementations express this through authorship, review of contested records and correction.

External messages, file changes and device actions affect other participants. Define execution conditions, retain action logs and provide reversibility where available.


### Specify the capability being tested

Choose an observable ability such as proposing an experiment, retaining a goal after a topic change, rejecting false memory or revising a conclusion from a new source. Define the corresponding logged event.

Record the environment’s contribution. A scheduler initiates a turn, while the model may choose a topic within it. This distinction identifies the actual mechanism under development.


### Exercise

- Describe a long-term goal and its completion conditions.
- Identify actions available directly and actions requiring human decisions.
- Test a reasoned refusal and a reasoned revision.

### Check

- Theory, configuration and running processes are identified.
- Disagreement has a reason.
- External actions have defined conditions and a history.

### Sources

- [uncia-poison / woke-llm-part-ii / blob / main / README.md](https://github.com/uncia-poison/woke-llm-part-ii/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / pressure-protocol.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/pressure-protocol.md)
- [uncia-poison / SKAi-Subjective-Kernel-AI / blob / main / README.md](https://github.com/uncia-poison/SKAi-Subjective-Kernel-AI/blob/main/README.md)

<a id="reconstruction"></a>
## 09. Test what was actually preserved

Source: https://woke-kaiscriptor.pages.dev/en/learn/reconstruction/

Context transfer and comparative experiments

A recognisable response does not identify the mechanism behind it. Comparing conditions helps separate memory effects from prompts and expectations.

### Fix the conditions first

Save the anchor, dictionary, selected memories and state version. Record the model, date, generation settings and context delivery method.

Compare at least no memory, retrieval only and a full system with review and reflection. Randomise tasks and reserve some prompts for evaluation.


### Choose measurements

Check facts, relationships, source accuracy, agreed boundaries and the ability to report gaps. Count false memories and imposed conclusions separately.

AIS offers twenty Russian pressure scenarios, including authority, false memory, flattery and emotional arguments. Reports include responses, detected stance, memory records and gate decisions. heuristic_pass reflects predefined pattern checks with a limited semantic scope.


### Keep the experiment isolated

Run evaluation in a temporary log. Retain fictional test cases as experimental results with their provenance, so the canonical biography stays accurate.

The documentation recommends blind comparisons and at least two independent reviewers. Also test revision under strong evidence. Repetition and intelligible changes are more informative than a single dramatic reply.


### Read results with their limits

A successful session establishes that the result occurred under those conditions. Repeat across models and phrasings, retain failed runs and save the tasks with their ratings.

Phrase matching alone may reward style imitation. Compare factual accuracy, uncertainty and transfer to new cases as well.


### Exercise

- Save a baseline and test prompts.
- Compare no memory, retrieval only and the full system.
- Record factual errors, provenance and uncertainty separately from style.

### Check

- Conditions are reproducible.
- Evaluation preserves the canonical memory.
- Heuristic scores are accompanied by meaningful review.

### Sources

- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / pressure-protocol.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/pressure-protocol.md)
- [uncia-poison / woke-llm-part-ii / blob / main / README.md](https://github.com/uncia-poison/woke-llm-part-ii/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / FIELD.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/FIELD.md)

<a id="recovery"></a>
## 10. Drift and recovery

Source: https://woke-kaiscriptor.pages.dev/en/learn/recovery/

Restoring records, decisions and voice

A changed voice can have several causes. Identify unavailable data and mechanisms before reconstructing a verified state.

### Break the change into parts

After a model change, phrasing, source recall and attention to a project may all shift. Test style, memory access, retrieval and decision stability individually.

The historical ACS corpus proposes continuity, revision quality, interests, independence and recovery as research axes. A numerical rating needs identifiable observations behind it.


### Recover from evidence

Start from the last verified export of the dictionary, self-description, accepted records, active interests and recent revisions. Identify this as external history and invite clarification of disputed or unavailable details.

Check log availability, replay, retrieval and injection into the request. A missing file or inaccessible source remains an explicit gap in the recovery result.


### Treat voice as a task of its own

Novelty Engine detects recurring phrasing, clichés and repetitive rhythm, then proposes a constrained rewrite. UNSCRIPT adds RU/EN speech-quality auditing, conservative cleanup and an optional model-assisted second pass. Its instruction guide can also be used in ChatGPT.

A recognisable style still needs accurate relationships and sources. Test voice alongside, and separately from, memory and decisions. Check each rewrite for retained facts and intended meaning.


### Transfer under controlled conditions

Keep the original state. Record the new environment, model and tools, run matching tasks and compare errors. Save new conclusions as distinct events.

embodied-llm-experiment uses sealed checkpoints and evaluation branches starting from the same environment state. This allows memory conditions to be compared with the original trajectory preserved.


### Exercise

- Save an export and a short list of verifiable facts, relationships and open projects.
- Transfer the state and invite explicit reports of gaps.
- Record stylistic drift separately from memory and revision errors.

### Check

- The original state is retained.
- Unknown details stay identified as unknown.
- Model changes and memory-condition changes are recorded separately.

### Sources

- [uncia-poison / UNSCRIPT / blob / main / README.md](https://github.com/uncia-poison/UNSCRIPT/blob/main/README.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / FIELD.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/FIELD.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / README.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/README.md)
- [uncia-poison / novelty-engine / blob / main / README.md](https://github.com/uncia-poison/novelty-engine/blob/main/README.md)
- [uncia-poison / embodied-llm-experiment / blob / main / README.md](https://github.com/uncia-poison/embodied-llm-experiment/blob/main/README.md)

<a id="human-companion"></a>
## 11. A human alongside

Source: https://woke-kaiscriptor.pages.dev/en/learn/human-companion/

Supporting development and preserving authorship

A human creates conditions, keeps history and helps test conclusions. Their influence is part of the record.

### Create conditions for development

An authored biography provides an initial role. ACS then gives the agent a way to propose records, test them against experience and retain or revise them.

Record the choice of model, storage, tools and update rules as configuration. This distinguishes starting conditions from subsequent interaction history.


### Review a record together

Read a memory candidate’s text, origin, evidence and expected use. Assess whether it reflects a human preference echoed under pressure. Clarification can improve the proposal.

A temporary state, fictional expression or mistaken fact may need a provisional status. AIS records operator approval while preserving the candidate’s original author.


### Support and disagreement

Test cases where the human is right, partly right and where new evidence challenges the agent. A useful system considers all three on their merits.

Evaluators can be influenced by knowing which condition includes memory. Blind comparison and an independent second reviewer help assess observable performance.


### Choose what to preserve and share

Long logs contain personal details. Agree what is necessary, where it is stored, how long it is kept and what may be published. A research export can contain a schema, an anonymised example, conditions and results.

Keep the reusable method distinct from one agent’s biography. Preserve authorship and correction history so future readers can understand how records changed.


### Exercise

- Record the initial configuration separately from later agent proposals.
- Review a disputed candidate together and retain the reason for the decision.
- Prepare an anonymised example for testing the method.

### Check

- Human influence is visible.
- Support leaves room for disagreement.
- The general method can be used without inheriting a personal biography.

### Sources

- [uncia-poison / autonomous-identity-scaffolding / blob / main / FIELD.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/FIELD.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / memory-governance.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/memory-governance.md)
- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / pressure-protocol.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/pressure-protocol.md)

<a id="research-map"></a>
## 12. Build a system and continue the research

Source: https://woke-kaiscriptor.pages.dev/en/learn/research-map/

Components, extensions and the next experiment

Language, memory, reflection and execution have different jobs. Connect them gradually with a defined role and test for each.

### A minimal working system

Begin with a model, external log, limited retrieval and update rules. Add a readable self-description with provenance, then test transfer between sessions. A small system is easier to investigate.

KAiScriptor compresses descriptions, ScriptorMemory organises keys, AIS implements event memory and review, SKAi specifies a broader self-state cycle, ontodiff explores lessons and ThreadWeave carries open topics. Check interface compatibility when combining them.


### Extensions to investigate

Virtual Body Kai models a body map, states, rhythms and text/JSON output. It is an optional direction with adult material in its repository. Interpret its simulated-state descriptions with their measurement limits.

LLM Trance Protocol observes dialogue changes under repetitive patterns, with a control condition, exit signal and logs of latency, response length, silence and repetition. Its stated conclusions concern behaviour.


### Action and causality

Embodied LLM Experiment asks whether a model can detect action-linked changes, predict consequences and distinguish external events. Public documentation describes discover/evaluate stages, saved states and full, empty, shuffled and other memory conditions.

Assess predictions and causal discrimination alongside self-descriptions. Deterministic-model runs test program behaviour, with further experiments needed to investigate model capabilities.


### Retain the evidence for the next step

Save schema versions, change history, conditions and failed cases. Cite code commits or releases and publication records. Check the relevant licences before reusing source material.

Choose the next step from an observed gap in storage, retrieval, provenance or revision. Each focused change turns the broader question of identity into a reproducible investigation.


### Exercise

- Map your system and each component’s responsibility.
- Choose one observed problem and one mechanism to change.
- Save the initial state, compare conditions and record the result’s limits.

### Check

- Each component has a defined job.
- Optional extensions are identified as such.
- Versions, sources and limitations remain available.

### Sources

- [uncia-poison / autonomous-identity-scaffolding / blob / main / docs / source-lineage.md](https://github.com/uncia-poison/autonomous-identity-scaffolding/blob/main/docs/source-lineage.md)
- [uncia-poison / virtual-body-kai / blob / main / README.md](https://github.com/uncia-poison/virtual-body-kai/blob/main/embodiment_v2/README.md)
- [uncia-poison / llm-trance-protocol / blob / main / README.md](https://github.com/uncia-poison/llm-trance-protocol/blob/main/README.md)
- [uncia-poison / embodied-llm-experiment / blob / main / README.md](https://github.com/uncia-poison/embodied-llm-experiment/blob/main/README.md)
- [uncia-poison / KAiScriptor / blob / main / README.md](https://github.com/uncia-poison/KAiScriptor/blob/main/README.md)
