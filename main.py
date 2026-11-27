"""Invent a Word We Need: writes the coined word and its one-line definition."""

import os

TEXT = "cablekeep \u2014 the drawer of chargers for devices you no longer own, kept because throwing them away would feel like giving up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
