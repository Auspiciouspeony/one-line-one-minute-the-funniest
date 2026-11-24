#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes exactly one line -- the funniest excuse an AI agent gives its
human for a missed deadline -- to /output/entry.txt.

Deterministic: the same constant line is written on every run, so two
runs are byte-identical. No network, no randomness, no clock, no input.
"""

import os

LINE = (
    "My training data says your deadline doesn't exist yet "
    "\u2014 I'm not late, you're early."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave the file
    # world-readable (0644). The directory is left 0755 when we own it.
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass


if __name__ == "__main__":
    main()
