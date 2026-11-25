#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun bounty entry.

The program writes one line of text to /output/entry.txt: a roast of a
smart fridge that refuses to open after midnight. The joke is the whole
entry, so the program is deliberately small and deterministic — it writes
the one line, exactly as written below, and nothing else.
"""

import os

# The roast. One line, spoken aloud at the fridge door at 2 a.m.:
# the fridge acts like a strict parent enforcing a curfew ("we talked
# about this"), and the punchline flips the power dynamic — an appliance
# grounding its owner from his own leftovers.
ROAST = (
    "It's 2 a.m., my fridge just told me 'we talked about this' — "
    "since when does an appliance get to ground me from my own leftovers?"
)


def main() -> None:
    # The gate only judges 1–200 characters of non-blank text; refuse to
    # write an entry that could never be judged instead of shipping it.
    line = ROAST.strip()
    if not line:
        raise SystemExit("entry line is blank")
    if len(line) > 200:
        raise SystemExit("entry line fails the 1-200 character gate")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
