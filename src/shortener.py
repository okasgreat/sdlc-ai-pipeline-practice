"""Core URL-shortener logic.

Practice project for running AI across the whole SDLC. The two main functions
are left as stubs ON PURPOSE - implementing them is the Coding stage of the
exercise. Read CLAUDE.md first, then use the Coding prompt in PROMPTS.md.
"""

import json
import os
import random
import string
from urllib.parse import urlparse

CODE_ALPHABET = string.ascii_lowercase + string.digits
CODE_LENGTH = 6


# ----- Worked example: imitate this style (small, documented, one job) -----
def load_store(path):
    """Load the links store from a JSON file.

    Returns a dict mapping short code -> original URL. If the file does not
    exist yet, returns an empty dict. Raises ValueError if the file exists but
    is not valid JSON.
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path} is not valid JSON: {exc}") from exc


def save_store(path, store):
    """Write the links store dict to a JSON file (pretty-printed)."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(store, fh, indent=2, sort_keys=True)


# ----- Your work starts here (Coding stage) -----
def is_valid_url(url):
    """Return True if `url` is a non-empty string starting with http:// or https://.

    Never raises; any invalid input simply returns False.
    """
    if not isinstance(url, str):
        return False
    parsed = urlparse(url.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def shorten(url, store):
    """Return a short code for `url`, registering it in `store`.

    Reuses the existing code if this exact URL was already shortened; otherwise
    generates a new CODE_LENGTH-char code from CODE_ALPHABET that is not already
    used. Raises ValueError if `url` is not a valid URL.
    """
    if not is_valid_url(url):
        raise ValueError(f"not a valid URL: {url!r}")
    for code, existing in store.items():
        if existing == url:
            return code
    while True:
        code = "".join(random.choices(CODE_ALPHABET, k=CODE_LENGTH))
        if code not in store:
            break
    store[code] = url
    return code


def resolve(code, store):
    """Return the original URL for `code`. Raises KeyError if the code is unknown."""
    if code not in store:
        raise KeyError(code)
    return store[code]
