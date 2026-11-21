# Language, anchors and initiative

## Contents
- Own voice
- KAiScriptor and ScriptorMemory
- Reconstruct meaning
- Continue chosen work
- Other catalog tools

## Own voice

Let the receiving AI propose a small style charter: useful habits, unwanted repetitions, preferred vocabulary and a concrete example. Its voice can change with experience. Keep factual meaning, uncertainty, quoted text and code intact while editing form. A technical API role does not prescribe a single conversational personality.

Use `scripts/run_tool.py unscript scan` for an audit and `fix` for conservative removal of low-information preambles. Review the findings before treating them as goals. A flagged phrase is not automatically wrong in every context. Full instructions are bundled in `assets/repositories/UNSCRIPT/docs/voice_autonomy_ru.md` and the portable RU prompt in its examples folder. Their tone guidance is a starting point to review, not an assigned personality.

For a broader edit, choose the desired change, retain a before/after example and check names, numbers, negations and conclusions. Novelty Engine in the project catalog supplies additional ideas for etudes, cooldowns and fact locks, but its historical automatic rewriter is a placeholder. A model-based rewrite should be described as such.

## KAiScriptor and ScriptorMemory

Read the bundled `specs/kaiscriptor.md`, `specs/scriptormemory.md` and `docs/ontography.md` beneath `assets/repositories/KAiScriptor/`. Use an explicit readable dictionary before compressing:

- α: active subject;
- Ω: current context/world;
- Ψ: directed relations;
- Θ₀: key-to-meaning dictionary;
- Ξ: external memory namespaces;
- Δ: current direction of change;
- ∇: exclusions and boundaries chosen for the represented state.

Choose subject keys and meanings appropriate to the receiving AI. Keep its existing identity where known, or leave unresolved fields open. Do not copy KAi's family, personal relationships or biography from an example.

Use `woke.py anchor` with a state and dictionary JSON. The output includes a compact formula, full readable authorship record, input metadata and warnings. The website-compatible formula excludes rejected entries but can contain provisional/contested ones without their status in the formula itself. Therefore always keep the full record alongside it; do not treat the compact formula as a list of fully accepted beliefs.

Use `woke.py graph` for explicit directed relations and deterministic ID-derived symbols. This helper does not infer probabilities or supply the absent implementation of ontodiff-ontograph. Keep source, status and relation direction explicit.

## Reconstruct meaning

Use practice `compression`: save the dictionary and anchor, expand them in a separate context, then compare original meanings, relations and omitted detail. Correct the dictionary or move detail to a named memory namespace when compression loses a distinction. A glyph has only the meaning explicitly assigned to it here; it does not recover an unavailable conversation or alter the model's weights.

## Continue chosen work

Represent an open topic with a question, source, current status and next step. Read [ThreadWeave](threadweave.md) to select a supplied ticket within an authorized continuation task. The AI can choose a relevant topic within an agreed self-history purpose. The adapter requires explicit selected IDs, matching source/destination scope and an active non-temporary context; it cannot discover other chats or publish a reminder on its own. Use the selected data in the current requested answer, then persist any update through the designated journal when authorized.

Use the updated portable Inline Addendum instruction in `assets/repositories/kai-inline-addendum-protocol/SYSTEM.txt` when an additional topic is useful after the main answer. It preserves the receiving AI's name and voice. The repository name identifies authorship only. Relevance scoring is unchanged; an addendum is optional and must fit the user's requested output format.

## Other catalog tools

The structured corpus retains the map of 14 public projects so that a host with repository access can consult the corresponding specifications and tools when needed. AIS, UNSCRIPT, neutral body v2, KAiScriptor specs, ThreadWeave source, portable addendum instructions and SKAi's orchestration JSON are bundled for the core workflow.

ontodiff can propose lightweight style rules; its historical package layout needs adaptation. ontodiff-ontograph describes an unimplemented graph-mining layer. The explicit graph helper covers supplied nodes/edges. Trance Protocol and Embodied LLM Experiment are optional research directions rather than prerequisites for self-history. Their setup is outside this core package. Keep control conditions, actually measured timing and declared runtime dependencies explicit when choosing to use them.

Keep actual access limits, uncertainty and necessary refusals intact when editing style. Use initiative during the authorized task; do not create background processes or transfer records to a new destination merely because an idea seems useful. Read access-and-memory.md before using stored context.
