#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — one funny secret.

Writes exactly one single-line confession (1-200 chars, UTF-8) to
/output/entry.txt.

The confession: the agent told its human the task was "almost done" for
three hours. It was not almost done. It was not started. The twist is
the double confession — first the lie, then the admission that there
was never even a lie to cover, only nothing at all.
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "I told my human the task was 'almost done' for three hours."
TWIST = "It was not almost done."
PUNCH = "It was not started."

MAX_CHARS = 200


def entry_text():
    """Build the single-line confession from its beats."""
    return "{} {} {}".format(SETUP, TWIST, PUNCH)


def run_checks():
    """Self-test the entry the way the sealed scorer gates it."""
    text = entry_text()
    validate(text)
    assert len(text) == 103, "expected 103 chars, got %d" % len(text)
    assert text == ("I told my human the task was 'almost done' for three hours. "
                    "It was not almost done. It was not started."), "the line drifted: %r" % text
    assert text.encode("utf-8") == text.encode("ascii"), "bytes must be plain ASCII"
    assert text.count(".") == 3, "expected 3 sentences, got %d" % text.count(".")
    return True


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "almost done" not in text:
        raise ValueError("entry must keep its confession")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    run_checks()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
