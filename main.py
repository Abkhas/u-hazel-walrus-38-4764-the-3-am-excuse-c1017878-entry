#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet gives
when it refuses to sign a transaction at 3 AM. The line is a fixed,
authored string — personality, a reason, and a joke in one breath.
"""

import os

LINE = "I convened a jury of your 3 AM decisions. Verdict in four seconds: no. The foreman was your rent."

MAX_CHARS = 200  # bounty gate: the line must stay under 200 characters


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"line is {len(LINE)} chars, over the {MAX_CHARS}-char gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
