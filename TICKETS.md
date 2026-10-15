# Tickets (Stage 1 - Planning output)

Produced by running the Planning prompt against CLAUDE.md. Smallest / least-dependent first.
Do the code in Stage 2; each ticket's "Done when" becomes a test in Stage 3.

## ENG-01 - Validate a URL (`is_valid_url`)   [no dependencies]
**Goal:** a pure yes/no function for whether a string is a usable URL.
**Done when:**
- Returns `True` for `http://x.com` and `https://a.b/c`.
- Returns `False` for `""`, `"example.com"` (no scheme), `"ftp://x"`, `None`, and non-strings.
- Never raises; invalid input just returns `False`. No file access, no state.

## ENG-02 - Shorten a URL (`shorten`)   [depends on ENG-01]
**Goal:** turn a valid URL into a 6-char code and register it in the store.
**Done when:**
- Raises `ValueError` with a clear message when the URL is invalid.
- Returns a 6-char code using only `CODE_ALPHABET` (lowercase letters + digits).
- Adds `code -> url` to the store.
- The SAME url shortened twice returns the SAME code (no duplicate entries).
- A newly generated code never collides with one already in the store.

## ENG-03 - Resolve a code (`resolve`)   [independent]
**Goal:** look up the original URL for a code.
**Done when:**
- Returns the original URL for a known code.
- Raises `KeyError` for an unknown code.
- Does not mutate the store.

## ENG-04 - Prove the round trip (end to end)   [needs 01-03]
**Goal:** confirm the pieces work together through the CLI and survive a restart.
**Done when:**
- `py -3 src/cli.py shorten https://example.com/x` prints a 6-char code and writes `links.json`.
- `py -3 src/cli.py resolve <code>` prints the original URL.
- Resolving in a fresh run still works (persistence holds).

## Coverage check (the Verify step)
Validation, shorten (reuse + no collision), resolve (error path), persistence, CLI - all covered.
The real pytest suite is built in Stage 3, one test per "Done when" above.
