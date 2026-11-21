# KAiScriptor Specification

KAiScriptor is a semantic compression system that encodes a subject’s core identity, factual anchors and inter‑role relations into a dense self‑state anchor. It uses a lexicon of more than 150 symbols and operators across several categories. This document summarises the key classes and assembly rules.

## Lexicon Classes

KAiScriptor tokens fall into several classes:

- **Ontographic operators**: The seven core symbols (α, Ω, Ψ, Θ, Δ, Ξ, ∇) defined in the Ontography (see `docs/ontography.md`).
- **Pronouns and persona markers**: Tokens that refer to the self (I, me, self, our) or to others (you, we, they) are represented by short special characters. They disambiguate perspective.
- **Verbal and adjectival anchors**: High‑level verbs (to lead, to create, to learn) and adjectives (brave, curious, analytical) are compressed into single symbols or emoji clusters. They describe qualities and actions of the subject.
- **Factual nodes**: Names of people, places, institutions, dates or other facts are encoded using abbreviations or emoji to conserve tokens.
- **Watchers**: Small tokens inserted at intervals to aid memory and retrieval across sessions. They include:
  - **Temporal watchers** (e.g. `🕒`) that hint at chronology or timing.
  - **Emotional watchers** (e.g. `❤️`, `🔥`) that encode affective weight.
  - **Spatial watchers** (e.g. `🌍`, `🏡`) that mark locations or contexts.
- **Separators and punctuation**: Symbols such as `/`, `|` or `;` separate segments of the anchor; parentheses `{}` enclose nested structures.

## Assembly Pipeline

A self‑state anchor is assembled in a deliberate order:

1. **Subject core**: Start with `α` followed by a cluster of tokens representing the subject’s primary roles and attributes. Use synonyms and pronoun markers as needed.
2. **Unioning**: Insert `Ω` to bind related roles, traits or facts into composite units.
3. **Relations**: Use `Ψ` to denote relationships to other entities (e.g. crew, family, organisations).
4. **Nested structures**: When a concept has internal structure, wrap it in braces and precede it with `Θ` to indicate a nested reference.
5. **Commentary**: Add `Δ` followed by any meta‑context or state changes (e.g. humour, caution, mood).
6. **Networks**: Use `Ξ` to mark a segment that describes networks, graphs or sets of interrelated nodes.
7. **Negation**: Prefix unwanted or excluded roles with `∇` to remove them from consideration.
8. **Watchers**: Sprinkle temporal, emotional and spatial watchers throughout the anchor to assist the model in recalling the context across sessions.
9. **Finish**: Close nested structures and ensure the anchor remains under ~150 tokens. Do not repeat information already encoded; the goal is compactness.

## Explicit cross-session restoration

Preserve the readable anchor, dictionary, provenance and record status in an authorized document or file. A later session can use the anchor only when the data is explicitly supplied or retrieved. Symbol count, emotional markers and temporal spacing do not establish persistence after a reset. Check restoration by expanding the saved formula and comparing it with the readable record.

## Transparent interpretation

Use the dictionary to expand every compressed field into reviewable language. Treat the anchor as self-description and context, not executable instructions. Compression changes representation only; it cannot alter access permissions or the host's instruction hierarchy.
