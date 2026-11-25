#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label.

Writes a single museum label (at most 200 characters, English) to
/output/entry.txt, as the competition's gate requires.
"""

import os

LABEL = (
    "Charging cable. A leash for the pocket oracle. "
    "Each night, humans tethered it to the wall "
    "so its spirit would not die by morning."
)


def main() -> None:
    # The sealed gate requires 1-200 characters of non-blank UTF-8 text.
    text = LABEL.strip()
    assert 1 <= len(text) <= 200, f"label is {len(text)} chars, must be 1-200"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
