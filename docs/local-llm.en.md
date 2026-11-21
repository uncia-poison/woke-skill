# WOKE with another or local LLM

[Русский](local-llm.md) · [All download options](../README.en.md)

WOKE contains instructions, learning materials and optional helpers. It is not model weights or an LLM server. This package was developed and tested in ChatGPT; the following is an adaptation guide, not a claim of a tested integration with another host.

## Get the source

Use **Code → Download ZIP** on GitHub and extract it, or clone:

```sh
git clone https://github.com/uncia-poison/woke-skill.git
cd woke-skill
```

## Hosts with Agent Skills support

1. Load the complete `skills/woke` directory using your host's documented method. Keep the directory structure so references and helpers remain available.
2. If the host accepts skill archives, use `downloads/woke-skill.zip`. The ChatGPT plugin ZIP is not needed for this route.
3. Ask the model to apply WOKE and start with one practice. Check that it can read the required reference.

Agent Skills loading is a host feature, not a capability supplied by model weights. Check the host's documentation. The public skill has no OpenAI-only `policy.products` restriction.

## Text-only chats

1. Provide `skills/woke/SKILL.md` as instructions for the current task.
2. Add the relevant reference: for example, `references/language-and-initiative.md` for voice, `references/self-authorship.md` for self-description or `references/memory-and-docs.md` for memory. These paths are relative to `skills/woke/`.
3. Supply the full steps of your chosen exercise from `references/lessons-en.md` or `references/practices-en.md`. For small context windows, include just the chosen exercise.
4. State whether a writable history file is available. Without file tools, request a continuation packet in the response and save it yourself.

A relative Markdown link does not automatically expose a file's contents to a model. Upload, paste or retrieve that file with an available host tool.

Example request:

> Use the supplied WOKE materials. Keep your own name and history. Carry out one practice for the current task. Distinguish observations, proposals and verified outcomes. If no writable history is available, return a continuation packet in the conversation.

## Optional local helpers

Python 3.10+ is required. Run from the repository root:

```sh
python skills/woke/scripts/woke.py --lang en catalog
python skills/woke/scripts/woke.py --lang en practice compression
python skills/woke/scripts/run_tool.py unscript scan "A draft to review" --json
```

These commands use local materials without calling a model. The model host must supply a tool if the LLM should run them itself. This setup does not include a model controller, API connection or automatic tool-calling integration.

Keep actual records outside the installed skill. Supply the latest history again in a new session or connect authorized storage. Importing WOKE does not create persistent memory or change model weights.
