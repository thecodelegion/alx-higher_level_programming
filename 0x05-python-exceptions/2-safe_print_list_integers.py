#!/usr/bin/python3


"""Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
        except IndexError:
            pass

        if count == x:
            break
    print()
    return count
