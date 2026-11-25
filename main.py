#!/usr/bin/env python3
"""One Word for the Boss entry.

The word is "omniscient": my boss knows everything -- except, somehow, how
to do my job. It is the funniest and truest single word for the boss everyone
has reported to at least once: the one with an opinion on every detail and
no doubt about any of it. It lands at lunch with no explanation needed, and
it works for a boss in a kitchen, a warehouse or an office alike.

Writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

WORD = "omniscient"


def main():
    # The gate allows 1-30 characters; a single word, no spaces, no newline.
    assert WORD and " " not in WORD and len(WORD) <= 30
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
