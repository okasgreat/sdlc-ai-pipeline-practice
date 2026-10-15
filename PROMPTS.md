# Prompts you can steal (one per stage)

Paste these into Cursor or Claude Code. They all assume your AI has read `CLAUDE.md`.
Swap `TICKET` / details for whatever you are working on.

## Stage 1 - Planning
```
Read CLAUDE.md. Break the URL-shortener spec in README.md into 3 to 5 small tickets,
smallest first. For each: a one-line goal and its acceptance criteria. Do not write code yet.
```

## Stage 2 - Coding
```
Implement is_valid_url, shorten, and resolve in src/shortener.py following CLAUDE.md.
Use the existing load_store/save_store style. Keep public signatures stable, standard
library only, add no new dependencies. Show me the diff before you touch anything else.
```

## Stage 3 - Testing
```
Write tests in tests/test_shortener.py using pytest. Cover the happy path, the failure
path, and two edge cases I would forget (same URL shortened twice returns the same code;
codes are 6 chars from the allowed alphabet). Run them and report what passes and what fails.
```

## Stage 4 - Debugging
```
Here is the failing output: <paste the actual pytest error>. Read the real error first,
find the root cause, and reproduce it as a failing test before you change any code. Then
fix it and show me the diff.
```

## Stage 5 - Deployment
```
Draft PR.md: summary, risk, rollback steps, and test evidence (paste the passing pytest
run). Flag anything that would need a human before this went to production.
```

## The red lines (do not cross)
- Secrets and keys: never in a prompt. Assume prompts leak.
- Customer data: redact before it touches a model.
- Production access: never direct. Staging first, human approval always.
- Review discipline: "it ran" is not "it is correct". You own the merge.
