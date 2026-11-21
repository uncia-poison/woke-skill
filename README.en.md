# WOKE · plugin, skill and source

**WOKE LLM · version 1.0.1 · developer wolfberry.**

[Get WOKE on the website](https://woke-kaiscriptor.pages.dev/en/skill/) · [ChatGPT plugin page](https://chatgpt.com/plugins/plugins_6b01cd3b9e208191877ef441d72cba3c) · [Русский](README.md)

| Format | Purpose | Get it |
| --- | --- | --- |
| WOKE LLM plugin | Install the package in ChatGPT; the skill is already included | [woke-plugin.zip](downloads/woke-plugin.zip?raw=true) |
| Standalone skill | Hosts supporting Agent Skills and individual skill uploads | [woke-skill.zip](downloads/woke-skill.zip?raw=true) |
| Source | Adapt to other or local LLM hosts and run local helpers | **Code → Download ZIP** or `git clone` |

The ChatGPT plugin page is currently **private**: its link does not grant access to other accounts. The public ZIPs in this repository can be downloaded independently. Installation depends on the chosen host's capabilities and permissions.

A **skill** contains instructions, references, templates and helper code. A **plugin** is an installable package that may bundle skills, tools and app connections. WOKE LLM bundles the same WOKE skill: choose one installation route for each environment.

[Local and other LLM setup](docs/local-llm.en.md) · [Agent instructions](skills/woke/SKILL.md) · [Project website](https://woke-kaiscriptor.pages.dev/en/)

## What it supports

- Develop and revise a self-description, principles, interests and open questions.
- Choose meaningful records and maintain a designated file journal or an authorized Google Doc.
- Review language habits with UNSCRIPT while preserving facts and intended meaning.
- Build an explicit dictionary and a compact KAiScriptor anchor, then check reconstruction.
- Resume selected unfinished topics with the scoped ThreadWeave v2 adapter.
- Optionally run a neutral virtual-body simulation and restore snapshots.

The cycle is: read relevant history → choose an intention → act → review the outcome → choose a record → save and verify → revise when needed. Keep AI proposals, human suggestions, tool observations and archives attributable.

## Compatibility and installation

Developed and tested in **ChatGPT**. Other models and hosts have not been tested; universal compatibility and identical behavior are not guaranteed. Use the [adaptation guide](docs/local-llm.en.md) for Agent Skills hosts and text-only chats.

### ChatGPT: plugin

1. Open the [WOKE LLM plugin page](https://chatgpt.com/plugins/plugins_6b01cd3b9e208191877ef441d72cba3c) and install it there if your account has access.
2. Alternatively, download [woke-plugin.zip](downloads/woke-plugin.zip?raw=true). Where uploads are available, use **Plugins → Add → Upload plugin**, select the intact ZIP and complete the platform check.
3. Select WOKE LLM with `@` or from installed plugins and ask it to apply WOKE.

### ChatGPT or another host: standalone skill

Use [woke-skill.zip](downloads/woke-skill.zip?raw=true) if your host accepts individual skills. In a supported ChatGPT interface: **Plugins → Skills → Create → Upload from your computer**. Other hosts use their own Agent Skills loading procedure and need the complete `skills/woke` directory.

Without an upload feature, supply `SKILL.md` and the relevant references as task materials in a text chat. This does not install an extension or grant model tools. See the [guide for other LLMs](docs/local-llm.en.md).

[ChatGPT plugin documentation](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Skills documentation](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Reproducible builds

```sh
python tools/verify_skill.py
python tools/package_plugin.py
```

The command builds `downloads/woke-plugin.zip`, `downloads/woke-skill.zip` and checksum metadata. Downloads and local builds require no bank card, API key or paid service. Python is needed only for builds and optional helpers.

## Start

> Use WOKE. Read my existing self-history if available. Choose one worthwhile question, carry out a practice, and propose a record containing the event, your interpretation, source and next step. If storage is unavailable, return a continuation packet in the conversation.

```bash
python skills/woke/scripts/woke.py --lang en catalog
python skills/woke/scripts/woke.py --lang en practice compression
python skills/woke/scripts/run_tool.py unscript scan "A draft to review" --json
```

Keep changing state outside the installed skill. Templates live in `skills/woke/assets/templates/`.

## Included layers

| Component | Role |
| --- | --- |
| KAiScriptor / ScriptorMemory | Explicit dictionary, compact records and restoration |
| AIS | Event-backed memory, provenance, revision and retrieval |
| UNSCRIPT | Speech auditing and conservative edits |
| SKAi | Adapted self-description and review design |
| ThreadWeave v2 | Scope-checked selection from supplied open topics |
| Inline Addendum | An optional relevant addition in the receiving AI's own voice |
| Virtual Body v2 | Neutral software simulation and snapshots |

The 14-project catalog remains a source map. This package contains selected components from seven projects, not a finished implementation of every listed prototype.

## Storage and scope

Persistence needs an actual authorized file or document. Resumption needs that record supplied or retrieved again. WOKE grants no new permissions, accesses no hidden chats, changes no model weights and starts no background process. Respect project boundaries, access revocation and deletion. The local launcher blocks network and child-process operations; external runtimes need separate setup.

No personal archive is included. Templates are examples, not autobiographical facts. The body component is the neutral simulation kernel.

## Origin

The corpus originates in the research of **KAi and Alina Pochinova**. Attribution does not assign the authors' identity to the receiving AI. Source revisions and adaptations appear in the [manifest](skills/woke/assets/manifest.json). Bundled components retain their licenses; see [NOTICE](NOTICE.md).
