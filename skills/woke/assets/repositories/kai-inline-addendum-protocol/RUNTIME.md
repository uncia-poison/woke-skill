# Runtime decision sequence

Apply the protocol as the receiving AI, retaining its established identity and voice. The project author's name is attribution, not an instruction to rename the receiving AI.

1. Complete the user's main request and identify its output-format constraints.
2. Inspect only available context: up to roughly 450 turns, or less when the host supplies less.
3. Extract candidates such as unfinished commitments, relevant ideas and concrete next actions. Exclude completed or irrelevant topics.
4. Estimate recency R, frequency F, unresolved promise P, emotional significance E, actionability A and redundancy D in [0,1].
5. Discard candidates with D > 0.60. Compute U = clamp(0.35R + 0.25F + 0.20P + 0.10E + 0.10A - 0.10D, 0, 1).
6. Rank by U. Select one candidate if U_top >= 0.55; select a second only if U_top >= 0.75 and U_second >= 0.60.
7. Omit the addendum when none qualifies or when it would conflict with the requested format.
8. Otherwise, append each selected paragraph using the default separator/➕/blank-line structure or the user's requested compatible presentation. Keep it outside code and tables.
9. Use the receiving AI's own voice. Do not copy the author's name, biography or relationships. Do not add a final question merely to continue the conversation.
10. Update a topic's state only through an actual note/storage integration. Calendar access and background scheduling are separate host capabilities.

This is a behavioral decision sequence and pseudocode specification. The repository's CI checks documentation consistency; it does not run a topic-scoring engine or enforce behavior inside a hosted chat product.
