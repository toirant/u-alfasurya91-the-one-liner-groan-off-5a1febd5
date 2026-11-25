#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke (max 140 characters) to
/output/entry.txt, exactly as the bounty gate requires: UTF-8 text,
one line, 1 to 140 characters, not only whitespace.

The joke: a calendar, stressed by too many dates. The pun lands in the
second half of the same line, so the setup and the turn both fit in one
breath, the way a dad delivers it at the dinner table.
"""

import os
import re

JOKE = (
    "I asked the calendar why it looked so stressed - "
    "it said too many dates, not enough time to itself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def tidy(text: str) -> str:
    """Collapse stray whitespace so the line stays a single clean line."""
    return re.sub(r"\s+", " ", text).strip()


def validate(joke: str) -> None:
    """Enforce the gate: one non-blank line of 1 to 140 characters."""
    if not joke:
        raise SystemExit("joke is empty")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} chars, over the 140 limit")


def main() -> None:
    joke = tidy(JOKE)
    validate(joke)
    # The grader mounts /output; create it if missing, never remove it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print(f"Wrote {len(joke)} chars to {OUTPUT_PATH}: {joke}")


if __name__ == "__main__":
    main()
