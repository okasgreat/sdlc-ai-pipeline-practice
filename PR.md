# PR: URL shortener, built across the five SDLC stages

## Summary
Implements the URL shortener from empty stubs, driven stage by stage with the Leverage Loop.
- `is_valid_url`, `shorten`, `resolve` implemented (stdlib only, per CLAUDE.md).
- `shorten` reuses the existing code for a repeat URL and avoids code collisions.
- Full pytest suite added: happy path, failure path, edge cases, persistence.
- Hardened the validator so a scheme with no host (e.g. `https://`) is rejected.

## Test evidence
```
$ py -3 -m pytest -q
..........                                                               [100%]
10 passed in 0.07s
```

## Risk
Low. This is an offline tool with no network, no database, and no third-party runtime
dependencies. The main correctness surface is URL validation; it is now parsed with
`urllib.parse.urlparse` and covered by tests, including the regression for scheme-only input.

## Rollback
No migrations, no infrastructure, nothing stateful to undo. To roll back, revert the
relevant commit(s):
```
git revert <commit-sha>      # or: git reset --hard <previous-sha> on a throwaway branch
```
The only runtime artifact is `links.json`, which is gitignored and safe to delete.

## Needs a human before production
Nothing in this exercise touches real production. But per the class red lines, if this were
a live service: never give the agent direct prod access, deploy to staging first, and a human
approves the merge. "It ran" is not "it is correct."

## Commit trail (the five stages)
- Scaffold: repo + context file + starter test
- Stage 1 (Planning): tickets from the spec
- Stage 2 (Coding): the three functions
- Stage 3 (Testing): full pytest suite
- Stage 4 (Debugging): reject scheme-only URLs, with a regression test
- Stage 5 (Deployment): this PR
