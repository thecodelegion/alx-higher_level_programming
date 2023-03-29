#!/usr/bin/python3


'''Definition: returns True for integers and False otherwise'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
