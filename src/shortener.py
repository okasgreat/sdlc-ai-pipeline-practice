"""Core URL-shortener logic.

Practice project for running AI across the whole SDLC. The two main functions
are left as stubs ON PURPOSE - implementing them is the Coding stage of the
exercise. Read CLAUDE.md first, then use the Coding prompt in PROMPTS.md.
"""

import json
import os
import string

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

    TODO (Coding stage): implement this. See the acceptance criteria in README.
    """
    raise NotImplementedError("Implement is_valid_url - see README and PROMPTS.md")


def shorten(url, store):
    """Return a short code for `url`, registering it in `store`.

    - Reuse the existing code if this exact URL was already shortened.
    - Otherwise generate a new 6-char code from CODE_ALPHABET that is not already used.
    - Raise ValueError if `url` is not a valid URL.

    TODO (Coding stage): implement this.
    """
    raise NotImplementedError("Implement shorten - see README and PROMPTS.md")


def resolve(code, store):
    """Return the original URL for `code`.

    Raise KeyError if the code is unknown.

    TODO (Coding stage): implement this.
    """
    raise NotImplementedError("Implement resolve - see README and PROMPTS.md")
