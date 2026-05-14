# Clipboard Text Transformer

Reads your clipboard, transforms the text, and writes it back.

## Setup

```bash
pip3 install pyperclip
```

## Usage

```bash
python3 transform.py <transform> [--preview]
```

| Transform | What it does |
|---|---|
| `uppercase` | Converts all text to uppercase |
| `bullets` | Turns each line into a bullet point |
| `strip` | Removes extra whitespace and blank lines |

| Flag | What it does |
|---|---|
| `--preview` | Prints the result without overwriting the clipboard |

## Example

```bash
python3 transform.py bullets --preview
python3 transform.py uppercase
```
