#!/usr/bin/python3
def write_file(filename='', text=''):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars = f.write(text)
        return num_chars
