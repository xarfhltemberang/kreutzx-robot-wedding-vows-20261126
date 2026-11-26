#!/usr/bin/env python3
"""Write one line of robot wedding vows to /output/entry.txt.

The vow is a single line of at most 160 characters, with no trailing
newline, exactly as the competition gate requires: a real promise, three
specific machine beats, and a payoff that twists the classic wedding
line in the final words.
"""

import os

ENTRY = (
    "I promise to love you through every update and every dead battery, "
    "and to hold your hand until death do us unplug."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= 160):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-160")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
