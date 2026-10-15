# Stage checklist

Tick each box as you finish it. Run the Leverage Loop (Context -> Constrain -> Generate -> Verify) every time.

## Stage 1 - Planning
- [ ] Read CLAUDE.md with your AI
- [ ] Broke the work into small tickets (smallest first)
- [ ] (Optional) connected Linear/Jira via MCP

## Stage 2 - Coding
- [ ] `is_valid_url` implemented
- [ ] `shorten` implemented (reuses existing code for a repeat URL)
- [ ] `resolve` implemented
- [ ] Reviewed the diff before accepting it

## Stage 3 - Testing
- [ ] Happy path test (shorten then resolve round-trips)
- [ ] Failure path test (bad URL raises ValueError; unknown code raises KeyError)
- [ ] Edge case: same URL twice returns same code
- [ ] Edge case: code is 6 chars from the allowed alphabet
- [ ] `py -3 -m pytest -q` is green

## Stage 4 - Debugging
- [ ] Reproduced one real bug as a failing test
- [ ] Read the actual error before guessing a fix
- [ ] Fixed it; the test now passes

## Stage 5 - Deployment
- [ ] `PR.md` written (summary, risk, rollback, test evidence)
- [ ] Nothing that needs a human was left unflagged
- [ ] Pushed to GitHub (see PUSH-TO-GITHUB.md)

## After
- [ ] Filled in METRICS.md and committed to the 30-day pact
