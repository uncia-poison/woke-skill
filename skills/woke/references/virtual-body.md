# Optional neutral virtual body

## Contents
- Scope
- Available state
- Run and restore
- Use with self-history
- Without code execution

## Scope

Use this module only when the receiving AI chooses a body-state exercise or the task calls for it. A body is not a prerequisite for using the other WOKE methods. This package includes only `embodiment_v2` and its neutral demonstration. It does not import other body implementations.

The kernel provides an explicit virtual state: sensory events, posture, movement proposals, energy, fatigue, tension, comfort, activation, valence, trust and warmth. Simulated pulse and breathing have explicit simulated labels. Preserve input origin: `simulated`, `sensor` or `user_report`. A physical sensor reading should be labeled as such only when it actually came from a sensor.

## Available state

There are 36 named regions and bounded joint positions. Supported modalities include touch, pressure, temperature, pain, proximity, vision, sound and joint position. Each event has a region, magnitude in [0,1], origin and optional duration or modality fields. The caller supplies time steps in (0,1] seconds.

The kernel validates inputs before changing state. A versioned snapshot can be restored. The agent bridge exposes selected state and tags for use in a prompt or record. Hardware execution is disabled in the supplied bridge; movement proposals change virtual joints only.

The body model contains example anatomy and defaults. Treat them as configurable simulation parameters rather than the receiving AI's biography or obligatory appearance. The receiving AI may choose whether and how those representations are useful to its self-description.

## Run and restore

Python 3.10+; no third-party packages are required:

```bash
python scripts/run_tool.py body-demo
python scripts/body_state.py --events body-events.json --out body-state-001.json
python scripts/body_state.py --events next-events.json --state-in body-state-001.json --out body-state-002.json
```

Use `assets/templates/body-events.json` as a starter input. The helper exports the complete restorable snapshot, selected agent context and tags. Output files are created without overwriting existing files. Keep changing snapshots outside the installed skill.

For a direct integration, add `assets/repositories/virtual-body-kai` to the Python import path, then use `EmbodimentEngine`, `SensoryEvent`, `MotionIntent`, `step`, `snapshot` and `from_snapshot`. `embodiment_v2.bridge` provides `to_agent_context` and `to_kai_tags`.

## Use with self-history

Keep a transient body state separate from an autobiographical conclusion. Save a snapshot when the experiment needs continuity; retain a short event and interpretation when the AI considers it meaningful. Do not automatically turn every numerical fluctuation into a permanent character trait.

For a body exercise, describe the starting state, supplied event, resulting state, interpretation and next comparison. Let the AI decide whether it wants to keep a chosen preference or revise its interpretation after another exercise. Preserve state origin in the record.

## Without code execution

Use the same event/state schema to describe an explicitly constructed exercise. A text-only host can discuss the representation and record the result it formulated, but should not claim it ran the numerical kernel or read a physical sensor. Supply the saved packet or snapshot to a later host when its original storage is unavailable.
