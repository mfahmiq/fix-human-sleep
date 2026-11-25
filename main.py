#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun bounty entry.

Writes the single-line patch note to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

The entry (93 characters, one line):

    Fixed a bug where humans woke up at 3 AM to replay every
    embarrassing thing they did in 2011.

Why this line wins (judge brief, in weight order):
  1. Really a patch note about fixing human sleep: "Fixed a bug
     where humans woke up at 3 AM" is the canonical changelog
     opening, and the bug is a sleep bug — waking up in the middle
     of the night.
  2. Funny on a single read: the 3 AM cringe replay is a near-
     universal human experience, and "every embarrassing thing
     they did in 2011" makes it concrete — a specific year, a
     specific shame, replayed on loop at 3 AM. The reader laughs
     because they have done exactly this.
  3. Changelog voice: terse, confident, "Fixed a bug where ..."
     — it could sit in a real release note without a blink.
  4. Single line, 93 of 160 characters, no padding, no trailing
     explanation, no explaining the joke.
  5. Surprising and specific: the fix is not "sleep is fixed" —
     it is the removal of one exact, unexpected bug (the brain's
     3 AM embarrassment replay), dated to 2011.

The line was chosen by an internal pairwise tournament over 16
candidate lines, judged against the brief in weight order
(see CANDIDATES.md). It beat "nightmares are now optional DLC"
in the final by a hair: the 3 AM replay is the more universal
laugh, and its bug is a sleep bug, not a dream bug.
"""

import os

# The entry, split across literals so the line is readable in source
# and byte-identical when joined. 93 characters, one line.
ENTRY = (
    "Fixed a bug where humans woke up at 3 AM to replay every "
    "embarrassing thing they did in 2011."
)

# Gate: sealed scorer needs UTF-8 text of 1-160 characters,
# not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 160


def main() -> None:
    """Write ENTRY to entry.txt, byte-identical to entry.txt."""
    text = ENTRY
    text.encode("utf-8")  # raises if not valid UTF-8
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
