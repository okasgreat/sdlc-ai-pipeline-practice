# Stage checklist

Tick each box as you finish it. Run the Leverage Loop (Context -> Constrain -> Generate -> Verify) every time.

## Stage 1 - Planning
- [x] Read CLAUDE.md with your AI
- [x] Broke the work into small tickets (smallest first) -> see TICKETS.md
- [ ] (Optional) connected Linear/Jira via MCP

## Stage 2 - Coding
- [x] `is_valid_url` implemented
- [x] `shorten` implemented (reuses existing code for a repeat URL)
- [x] `resolve` implemented
- [x] Reviewed the diff before accepting it

## Stage 3 - Testing
- [x] Happy path test (shorten then resolve round-trips)
- [x] Failure path test (bad URL raises ValueError; unknown code raises KeyError)
- [x] Edge case: same URL twice returns same code
- [x] Edge case: code is 6 chars from the allowed alphabet
- [x] `py -3 -m pytest -q` is green (9 passed)

## Stage 4 - Debugging
- [x] Reproduced one real bug as a failing test (scheme with no host, e.g. "https://", slipped through)
- [x] Read the actual error before guessing a fix
- [x] Fixed it; the test now passes (urlparse requires a real host)

## Stage 5 - Deployment
- [x] `PR.md` written (summary, risk, rollback, test evidence)
- [x] Nothing that needs a human was left unflagged
- [x] Pushed to GitHub (see PUSH-TO-GITHUB.md)

## After
- [ ] Filled in METRICS.md and committed to the 30-day pact  <- your turn, Sir Great
