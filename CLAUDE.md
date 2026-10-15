# CLAUDE.md - Context file for this repo

> This is the "genius intern" briefing. Your AI has never seen this project and forgets
> everything between sessions. Keep this file current and point the AI at it every stage.
> This is the single biggest payoff of the class: write the context once, reuse it everywhere.

## Project overview

- **What this is:** a tiny URL shortener used to practise running AI across the whole SDLC.
- **Stack:** Python 3 standard library only, plus `pytest` for tests. No web framework, no database.
- **Storage:** a JSON file on disk (`links.json` by default).
- **Entry points:** `src/shortener.py` (the logic), `src/cli.py` (the command line).
- **Goal:** working `shorten()` and `resolve()` with real tests, driven through all five pipeline stages.

## Guidelines

- Run Python as `py -3` on this machine (bare `python` is a hijacked environment).
- Standard library only in `src/`. The only third-party dependency allowed is `pytest`, and only under `tests/`.
- Keep public function signatures stable once written (other code and tests depend on them).
- Short codes are 6 characters, lowercase letters and digits.
- Every function has a docstring saying what it does, its inputs, and what it raises.
- Tests live in `tests/`, run with `py -3 -m pytest -q`.

## Constraints (what not to touch / assume)

- Do not add a web server, Flask, FastAPI, or any network code. This is offline.
- Do not invent a database. Persistence is the JSON file, nothing more.
- Do not silently swallow errors. Invalid input raises `ValueError` with a clear message.
- Do not assume a URL is valid because it is a non-empty string. Check it starts with `http://` or `https://`.
- Never commit a real secret or key. There are none in this project; keep it that way.

## Examples

- **Good pattern to imitate:** `load_store()` in `src/shortener.py` - small, documented, one job, raises on bad input.
- **Bad pattern to avoid:** a function that both computes a value and writes a file and prints to screen. Keep one job per function.
