#!/usr/bin/env python3
"""Clipboard Text Transformer: read clipboard, transform it, write it back."""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Transform clipboard text."
    )

    # choices= means argparse will reject anything not in this list
    # and print a helpful error message automatically
    parser.add_argument(
        "transform",
        choices=["uppercase", "bullets", "strip"],
        help="Transformation to apply: uppercase | bullets | strip"
    )

    args = parser.parse_args()
    print(f"Transform selected: {args.transform}")


if __name__ == "__main__":
    main()