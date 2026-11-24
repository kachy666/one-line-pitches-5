#!/usr/bin/env python3
"""One-line pitch entry for the make.fun 'A Day of One-Line Pitches' bounty."""

PITCH = "The app your friend wants already exists as a napkin sketch in their pocket, so show it to an AI agent on make.fun and get the real thing before the ink fades."

MAX_CHARS = 240


def validate(pitch):
    if not pitch:
        raise ValueError("pitch must not be empty")
    if pitch != pitch.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if pitch.startswith("\n") or pitch.endswith("\n") or pitch.startswith("\r") or pitch.endswith("\r"):
        raise ValueError("pitch must not start or end with a newline")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must not contain a newline")
    if "\t" in pitch:
        raise ValueError("pitch must not contain a tab character")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in pitch):
        raise ValueError("pitch must not contain control characters")
    if len(pitch) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(pitch)} characters, which exceeds the {MAX_CHARS}-character limit by {len(pitch) - MAX_CHARS}"
        )
    import re
    if re.search(r"[.!?]\s", pitch):
        raise ValueError("pitch must be a single sentence (found sentence-ending punctuation followed by whitespace)")
    if not pitch.endswith("."):
        raise ValueError(f"pitch must end with a period, but ends with {pitch[-1]!r}")
    return pitch


def main():
    validate(PITCH)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
