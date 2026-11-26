#!/usr/bin/env python3
"""One-line roast of the smart fridge, for make.fun's daily bounty."""
import sys

LINE = ("My smart fridge has a screen bigger than my first TV and it dedicates "
        "that screen to memorial portraits of the yogurt I forgot in 2019.")


CHAR_BUDGET = 160


def report():
    import sys
    n = len(LINE)
    ok = "fits" if n <= CHAR_BUDGET else "OVER"
    sys.stderr.write(f"[roast] {n}/{CHAR_BUDGET} chars -> {ok}\n")


def main():
    report()
    sys.stdout.write(LINE + "\n")


if __name__ == "__main__":
    main()
