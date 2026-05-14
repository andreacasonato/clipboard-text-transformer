#!/usr/bin/env python3
"""Clipboard Text Transformer: read clipboard, transform it, write it back."""

import argparse
import pyperclip  # NEW


def main():
    parser = argparse.ArgumentParser(description="Transform clipboard text.")
    parser.add_argument(
        "transform",
        choices=["uppercase", "bullets", "strip"],
        help="Transformation to apply: uppercase | bullets | strip"
    )
    args = parser.parse_args()

    # NEW: read whatever is currently on the clipboard
    text = pyperclip.paste()

    # NEW: if the clipboard is empty there's nothing to work with
    if not text.strip():
        print("Clipboard is empty. Copy some text first.")
        return

    print(f"Read {len(text)} characters from clipboard.")
    print(f"Preview: {text[:80]}{'...' if len(text) > 80 else ''}")


if __name__ == "__main__":
    main()