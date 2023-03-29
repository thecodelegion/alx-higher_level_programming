#!/usr/bin/python3


"""Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(my_list[i], end='')
            i += 1
    except IndexError:
        pass
    finally:
        print(' ')
    return i
