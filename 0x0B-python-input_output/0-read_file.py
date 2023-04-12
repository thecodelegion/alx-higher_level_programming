#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        print(text)
