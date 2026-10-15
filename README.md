# SDLC + AI Pipeline Practice

A hands-on exercise for running AI across the **whole** software pipeline, not just the coding step.

Built from the Outskill masterclass "Manage Your SDLC Pipeline with AI". The goal is not to finish an app. The goal is to **run the Leverage Loop at every stage** on a small, real project until the method is muscle memory.

## The one method (do this at every stage)

**Context -> Constrain -> Generate -> Verify**

1. **Context** - brief your AI like a new intern: the task, the repo, the patterns. (It reads `CLAUDE.md`.)
2. **Constrain** - hand it the rules: what not to touch, what not to assume.
3. **Generate** - let it plan, code, test, or fix.
4. **Verify** - read it, run it, prove it. "It ran" is not "it is correct". You own the merge.

## What you are building

A tiny **URL shortener** (like the getowl.ai demo from class). No web framework, no database, pure Python plus a JSON file. Small enough to finish one stage per sitting.

It should:
- Take a long URL and return a short code (e.g. `https://example.com/very/long` -> `a1b2c3`).
- Resolve a short code back to the original URL.
- Reject rubbish input (not a URL, empty string).
- Persist links to a JSON file so they survive a restart.
- Be driven from a small command-line interface.

Starter stubs are in `src/`. They raise `NotImplementedError` on purpose. **That is the work.**

## The exercise: walk all five stages

Do them in order. Use the matching prompt from `PROMPTS.md`. Tick the boxes in `STAGES.md` as you go.

| Stage | You produce | Tool from class |
|---|---|---|
| 1. Planning | A short spec / ticket for the next piece of work | Linear / Jira MCP (optional) |
| 2. Coding | `shorten()` and `resolve()` implemented to spec | Cursor (steer) or Claude Code (drive) |
| 3. Testing | `tests/test_shortener.py` covering happy path, failure path, 2 edge cases | your AI + `pytest` |
| 4. Debugging | A real bug reproduced as a failing test, then fixed | read the actual error first |
| 5. Deployment | A PR description with summary, risk, rollback, test evidence | draft in `PR.md` |

## How to run it

```bash
# from the repo root
py -3 -m pip install -r requirements.txt   # installs pytest
py -3 -m pytest -q                         # run the tests (they will fail until you build)
py -3 src/cli.py shorten https://example.com/some/long/link
py -3 src/cli.py resolve a1b2c3
```


The honest question to leave with: **is this actually faster, or does it just feel faster?**
