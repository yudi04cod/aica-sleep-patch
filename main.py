#!/usr/bin/env python3
"""Aica Sleep Patch — writes one funny patch note announcing human sleep is fixed.

Deterministic: the same bytes are written on every run.
Python 3.13, standard library only, no network.
"""

import os
import sys

PATCH_NOTE = (
    "Fixed: 8 hours of sleep now restores more than 0% energy. "
    "Removed the 3 a.m. overthinking DLC \u2014 it kept reinstalling itself."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(note: str) -> None:
    """The gate wants 1-160 chars of UTF-8, not only whitespace, one line."""
    if not note.strip():
        raise ValueError("patch note must not be blank")
    if len(note) > MAX_CHARS:
        raise ValueError(
            f"patch note is {len(note)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in note or "\r" in note:
        raise ValueError("patch note must be a single line")


def main() -> int:
    validate(PATCH_NOTE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PATCH_NOTE)
    print(f"wrote {len(PATCH_NOTE)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
