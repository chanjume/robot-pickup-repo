#!/usr/bin/env python3
"""Write one original robot pickup line to /output/entry.txt.

The line is a pickup line in a robot's own voice. The joke turns on
the robot's own situation: it ran 10,000 simulations of asking
someone out, and in 9,999 of them the answer was yes -- then admits
this attempt is the one simulation left, the one where the answer was
no. Two concrete numbers plus a twist in the last clause that
redefines the whole setup. One line, under 200 characters.
"""
import os

LINE = "I ran 10,000 simulations of asking you out. In 9,999 of them, you said yes. This is the other one."
# 101 chars: the robot confesses, with numbers, that this is the losing simulation.


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
