# -*- coding: utf-8 -*-
"""Parsing methods package."""


def parse_operation(operation_string):
    """
    Parses an arithmetic operation string and returns the operands and operator.
    """
    op_list = operation_string.split(" ")
    first_num = int(op_list[0])
    operator = op_list[1]
    second_num = int(op_list[2])

    return first_num, second_num, operator
