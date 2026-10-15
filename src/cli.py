"""Tiny command-line interface for the URL shortener.

Usage:
    py -3 src/cli.py shorten <url>
    py -3 src/cli.py resolve <code>

Uses links.json in the current directory as the store. This wiring is done for
you so you can focus on the logic in shortener.py.
"""

import sys

from shortener import load_store, save_store, shorten, resolve

STORE_PATH = "links.json"


def main(argv):
    if len(argv) != 2:
        print("usage: cli.py [shorten <url> | resolve <code>]")
        return 1

    command, value = argv
    store = load_store(STORE_PATH)

    if command == "shorten":
        try:
            code = shorten(value, store)
        except ValueError as exc:
            print(f"error: {exc}")
            return 1
        save_store(STORE_PATH, store)
        print(code)
        return 0

    if command == "resolve":
        try:
            print(resolve(value, store))
        except KeyError:
            print(f"error: unknown code {value!r}")
            return 1
        return 0

    print(f"error: unknown command {command!r}")
    return 1


if __name__ == "__main__":
    # allow running from the repo root: python src/cli.py ...
    sys.path.insert(0, __file__.rsplit("cli.py", 1)[0])
    raise SystemExit(main(sys.argv[1:]))
