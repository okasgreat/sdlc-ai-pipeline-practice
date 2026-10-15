"""Tests for the URL shortener (Stage 3 - Testing).

One test per acceptance criterion in TICKETS.md: happy path, failure path, edges.
Run with:  py -3 -m pytest -q
"""

import os
import sys

import pytest

# make src/ importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from shortener import (  # noqa: E402
    CODE_ALPHABET,
    CODE_LENGTH,
    is_valid_url,
    load_store,
    save_store,
    shorten,
    resolve,
)


# ----- ENG-01: is_valid_url -----
def test_valid_url_accepts_http_and_https():
    assert is_valid_url("http://x.com")
    assert is_valid_url("https://a.b/c")


def test_valid_url_rejects_bad_input():
    for bad in ["", "example.com", "ftp://x", None, 123, ["http://x"]]:
        assert is_valid_url(bad) is False


# ----- ENG-02: shorten -----
def test_shorten_returns_six_char_code_from_alphabet():
    code = shorten("https://example.com/x", {})
    assert len(code) == CODE_LENGTH
    assert all(ch in CODE_ALPHABET for ch in code)


def test_shorten_same_url_returns_same_code():
    store = {}
    first = shorten("https://example.com/x", store)
    second = shorten("https://example.com/x", store)
    assert first == second
    assert len(store) == 1  # no duplicate entry


def test_shorten_invalid_url_raises_valueerror():
    with pytest.raises(ValueError):
        shorten("not-a-url", {})


# ----- ENG-03: resolve -----
def test_resolve_round_trip():
    store = {}
    code = shorten("https://example.com/x", store)
    assert resolve(code, store) == "https://example.com/x"


def test_resolve_unknown_code_raises_keyerror():
    with pytest.raises(KeyError):
        resolve("zzzzzz", {})


# ----- ENG-04: persistence -----
def test_persistence_round_trip(tmp_path):
    path = str(tmp_path / "links.json")
    store = {}
    code = shorten("https://example.com/persist", store)
    save_store(path, store)
    reloaded = load_store(path)
    assert resolve(code, reloaded) == "https://example.com/persist"


def test_load_store_missing_file_returns_empty(tmp_path):
    assert load_store(str(tmp_path / "nope.json")) == {}
