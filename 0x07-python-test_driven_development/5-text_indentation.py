#!/usr/bin/python3
"""function prints a text..."""

def text_indentation(text):
    """prints text with 2 new lines after each `.`, `?` and `:`.
    Args:
        text(str): the string passed.
    """
    char = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in char:
        if c in text:
            split_text = text.split(c)
            text = str()
            for i in range(len(split_text) - 1):
                text += f"{split_text[i].strip()}\n\n"
            text += f"{split_text[i + 1].strip()}"
        print(text)
