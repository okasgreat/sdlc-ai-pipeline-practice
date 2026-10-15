"""Tests for the URL shortener.

Only ONE starter test is written, and it is for the worked example (load_store).
The rest is your Testing stage: use the Testing prompt in PROMPTS.md to have your
AI generate the happy path, the failure path, and two edge cases you would forget.

Run with:  py -3 -m pytest -q
"""

import os
import sys

# make src/ importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from shortener import load_store  # noqa: E402


def test_load_store_missing_file_returns_empty(tmp_path):
    missing = tmp_path / "nope.json"
    assert load_store(str(missing)) == {}


# TODO (Testing stage): add tests for is_valid_url, shorten, and resolve.
#   - happy path: a good URL shortens, then resolves back to the same URL
#   - failure path: a bad URL raises ValueError; an unknown code raises KeyError
#   - edge cases: the SAME url shortened twice returns the SAME code;
#                 codes are 6 chars from the allowed alphabet
