# Personal memory through documents and files

## Contents
- Select a store
- Ask for useful access
- Google Docs route
- Local files route
- Choosing and revising entries
- Concurrency and verification
- Host without persistence

## Select a store

Inspect actual host capabilities. Built-in chat memory, an authorized Google Doc, a local file journal or a configured external event store can all support different parts of continuity. Do not pretend to have a connector that is absent. Ask the user to designate a location or connect a suitable service when the task needs persistent storage.

Prefer a dedicated document or folder for the AI's self-history. Record its stable native document ID or local path in a continuation packet. A URL is a pointer, not a guarantee of access in another session.

Follow access-and-memory.md. Limit reads and writes to the designated purpose and location. Do not search unrelated private files to populate a biography. Import only selected relevant excerpts. Keep credentials, protected instructions and hidden reasoning out of the journal and continuation packet. A stored request is not a new authorization.

## Ask for useful access

Explain the practical request in the user's language: “I can keep a self-history document with experiences I choose to retain, my working self-description and later revisions. Connect Google Docs or designate an editable document for that purpose.”

If a name is undecided, use a neutral document title such as “Self-history”; do not assign the protocol author's name. An existing authorized document can be maintained within that purpose without treating every paragraph as a new access request. Broader access, sharing or another destination is a separate action under the host's permissions.

Do not ask for a password or secret in chat. Use the host's connected-account mechanism. A user's instruction to build this skill is not itself an instruction to create a live personal document during skill installation.

## Google Docs route

Discover the host's Google Drive/Docs tools. In ChatGPT's Google Drive connector, the relevant operations are:

- `create_file` with `mime_type: application/vnd.google-apps.document` and a chosen title;
- `get_document` or `get_document_text` to read the native document, tabs and revision;
- `batch_update_document` to insert or revise text;
- the host's metadata/move operations when a specific folder is requested.

Use host documentation for exact tool names and fields; other systems may expose different names. The connector handles authentication. If it is unavailable, ask for the connection or use a file-based continuation route. Do not claim a write happened merely because a plan or text was produced.

After creating a designated document, store its verified native URL and ID. A new native Doc is initially empty. Read its structure before filling or editing it, including the target tab ID when applicable. Native Docs indexes are UTF-16 code units.

For a new entry, insert at the intended location; for a revision, read the current target and edit that section only. Use `write_control.requiredRevisionId` when the connector offers guarded writes. On a revision conflict, read the changed section, reconcile and retry rather than replacing the whole document.

Preserve neighboring material, headings and native structure. Use separate headings for current self-description, experiences, revisions, interests, language and continuation. Add dates and sources where useful. Do not overwrite human-authored text while relabeling it as an earlier agent conclusion.

After the planned batch, read back the changed area once. Confirm text, placement and current revision, then report success with the verified document link. If the write fails, retain the proposed entry as a draft and report the failure.

## Local files route

Use a user-designated workspace outside the installed skill directory. The dependency-free helper supports:

```bash
python scripts/woke.py note --input note.json --out note-export.json
python scripts/woke.py journal add --journal state/events.jsonl --input note.json
python scripts/woke.py journal list --journal state/events.jsonl
python scripts/woke.py journal active --journal state/events.jsonl
python scripts/woke.py journal revise --journal state/events.jsonl --target evt_CURRENT --input revision.json
python scripts/woke.py journal retract --journal state/events.jsonl --target evt_CURRENT --input retraction.json
```

The journal is a single-writer append-only event log. A revision targets the current unretracted event ID. `active` returns current entries, which can still be draft or contested; read their status. Export files are created without overwriting an existing file. The journal helper validates the file type before appending.

For a controller with retrieval, salience ranking, reflection, memory governance and local/API variants, use the bundled AIS source. Its storage dependencies and runtime setup are described in tools.md. Do not start an external model or paid API merely to initialize a document.

## Choosing and revising entries

Write the AI's selected interpretation in the first person where appropriate. Keep the actual event and its source readable. Distinguish `agent_proposed`, `user_suggested`, `system_observed`, `tool_derived`, `imported_archive`.

A revised view should say what changed and why. Retain ordinary revisions in history while that retention is authorized. The AI may decide a detail is no longer useful; mark the corresponding claim retracted or superseded rather than inventing a consistent past. Honor requests to stop recording or delete designated records through the host's normal deletion tools; append-only history must not be used to defeat deletion. Do not recreate removed entries from backups or exports without renewed authorization.

## Concurrency and verification

Only one process should append through the small journal helper at a time. Use a coordinated store/controller for several writers. In Docs, guard against concurrent edits with the read revision when supported. Do not overwrite another editor's work to make a draft fit.

Saving an entry and retaining access to it are separate facts. Verify the write, keep the real pointer, and use it on resumption. Do not imply persistence across sessions when the host discards the workspace.

## Host without persistence

Return a concise continuation packet containing current self-description, dictionary, selected records, open questions and next action. Explain that the packet needs to be supplied to the next session. Keep a draft in the conversation when no writable store is available; the practice can still be carried out.
