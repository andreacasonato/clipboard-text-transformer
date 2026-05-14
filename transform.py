#!/usr/bin/env python3
"""Clipboard Text Transformer: read clipboard, transform it, write it back."""

import argparse
import pyperclip


# Each transformation is its own function.
# str.upper() returns a NEW string, it never modifies the original.
# Strings in Python are immutable, so every string method always returns a new one.
def transform_uppercase(text: str) -> str:
    return text.upper()


# This function maps the CLI argument to the right transformation function.
# We'll add bullets and strip here in the next steps.
def apply_transform(transform: str, text: str) -> str:
    if transform == "uppercase":
        return transform_uppercase(text)

    print(f"'{transform}' not implemented yet.")
    return text


def main():
    parser = argparse.ArgumentParser(description="Transform clipboard text.")
    parser.add_argument(
        "transform",
        choices=["uppercase", "bullets", "strip"],
        help="Transformation to apply: uppercase | bullets | strip"
    )
    args = parser.parse_args()

    text = pyperclip.paste()
    if not text.strip():
        print("Clipboard is empty. Copy some text first.")
        return

    result = apply_transform(args.transform, text)
    print(result)


if __name__ == "__main__":
    main()