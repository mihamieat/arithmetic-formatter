# -*- coding: utf-8 -*-
"""Formating modules."""


# -*- coding: utf-8 -*-
def display_line(line: list, space: int = 0):
    """Return a string of each element in the given line with an optional leading space."""
    for values in line:
        return " " * space + values


def display_dashes(occurrences: int):
    """
    Returns a string consisting of dashes repeated a specified number of times.
    """
    return "-" * occurrences


def number_of_dashes(num1: str, num2: str):
    """
    Returns the number of dashes required to represent the maximum length between two numbers.
    """
    return (
        # max(len(num1), len(num2), len(result)) + 1
        # if resolved
        max(len(num1), len(num2))
        + 2
    )


def first_line(nnb_of_dashes: int, num1: str):
    """
    Returns the first line of an arithmetic expression
    formatted with the given number of dashes and the first number.
    """
    number_of_spaces = nnb_of_dashes - len(num1)
    return f"{' ' * number_of_spaces}{num1}"


def second_line(nb_of_dashes: int, num2: str, operator: str):
    """
        Returns the second line of an arithmetic expression
        formatted with the given number of dashes, the
    second number, and the operator.
    """
    number_of_space = nb_of_dashes - len(num2) - 1
    return f"{operator}{number_of_space * ' '}{num2}"


def result_line(nb_of_dashes: int, result: str):
    """
    Returns the line displaying the result of an arithmetic
    expression formatted with the given number of dashes.
    """
    number_of_spaces = nb_of_dashes - len(result)
    return f"{' '*number_of_spaces}{result}"
