"""Charm the Commuter: a one-line forecast for a city that isn't.

The program writes a single deterministic line of weather for
Nowhereville, a city that does not exist, to /output/entry.txt.

Python 3.13, standard library only. No input, no network, no
randomness: every run produces the exact same bytes.
"""

import os

LINE = (
    "Good morning, Nowhereville: fog lifts by 8, sunshine by 9, "
    "and your train pulls in at 8:47 - on time, for once."
)

def main() -> None:
    """Write the forecast line to /output/entry.txt, exactly one line."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
