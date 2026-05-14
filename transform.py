#!/usr/bin/env python3
"""Clipboard Text Transformer: read clipboard, transform it, write it back."""

import argparse
import re
import pyperclip


def transform_uppercase(text: str) -> str:
    return text.upper()


def transform_bullets(text: str) -> str:
    lines = text.splitlines()
    bulleted = [f"• {line.strip()}" for line in lines if line.strip()]
    return "\n".join(bulleted)


def transform_strip(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(lines)
    return text.strip()


def apply_transform(transform: str, text: str) -> str:
    if transform == "uppercase":
        return transform_uppercase(text)
    if transform == "bullets":
        return transform_bullets(text)
    if transform == "strip":
        return transform_strip(text)
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

    # Write the transformed text back to the clipboard
    # After this line the user can paste the result anywhere immediately
    pyperclip.copy(result)
    print(f"Done. ({len(text)} chars --> {len(result)} chars)")


if __name__ == "__main__":
    main()