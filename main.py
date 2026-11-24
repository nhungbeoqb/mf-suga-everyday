#!/usr/bin/env python3
"""Everyday Things, Two Lines — entry program.

Writes a two-line explanation of a queue to /output/entry.txt.
Line 1: one vivid sentence explaining a queue to a 10-year-old through
a single concrete analogy. Line 2: one sentence on what the analogy
maps and what it leaves out.
"""

import os

ENTRY = (
    "A queue is a train made of people: each person hooks on behind the one "
    "in front, and the whole train only moves as fast as the person at the "
    "very front.\n"
    "The train fits because both travel in single file and take turns at "
    "the front, but it leaves out the engine \u2014 a queue has no driver, "
    "it only moves because each person chooses to step forward.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
