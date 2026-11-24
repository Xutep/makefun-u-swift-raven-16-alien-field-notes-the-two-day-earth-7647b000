#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt. Deterministic, stdlib-only, no input, no network.
"""

import os

# One original line, 167 characters: an alien tourist's review of Earth.
# The laugh comes from the alien's angle on ordinary Earth life (the
# glowing box humans stare at all day), it reads like a real review with
# a verdict, and the punch lands at the end.
REVIEW = (
    "The locals built a glowing box that shows them strangers living "
    "better lives, then stare at it all day feeling worse. "
    "I stared too. Five stars, would doomscroll again."
)


def main() -> None:
    text = REVIEW.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("review must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(text))


if __name__ == "__main__":
    main()
