"""Everyday Wonder entry: write one sentence about a small everyday
moment of wonder to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)."""

import os

SENTENCE = (
    "At 6 a.m. the street sweeper sang to his broom, "
    "and the whole empty road sounded briefly like it had a soundtrack."
)


MAX_CHARS = 200


def validate_sentence(sentence):
    """One sentence, 1-200 chars, no internal newline."""
    text = sentence.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of range"
    assert "\n" not in text, "sentence must not contain a newline"
    return text


def write_entry(sentence, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    return path


def main():
    sentence = validate_sentence(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(sentence, out_dir)
    print(f"Wrote {len(sentence)} characters to {path}")


if __name__ == "__main__":
    main()
