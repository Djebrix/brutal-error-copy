#!/usr/bin/env python3
"""Writes one line of brutal, funny error copy to entry.txt.

Deterministic, stdlib only, no network.
"""
import os

LINE = (
    "We saved your file, then lost the disk we saved it on. "
    "The backup was on the same disk. Please type it all again."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
