#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Prints a single funny warning label for humans. Pure standard library,
deterministic: the same line, byte for byte, on every run.
"""

# The entire entry: exactly one line of output, no trailing spaces,
# no randomness, no input read. Safe to run anywhere.
LABEL = (
    "WARNING: This human runs on caffeine and confidence, contains opinions "
    "formed entirely from headlines, and may spontaneously say "
    "'per my last email' \u2014 side effects include eye-rolls and sudden silence."
)


def main() -> None:
    print(LABEL)


if __name__ == "__main__":
    main()
