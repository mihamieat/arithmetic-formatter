# -*- coding: utf-8 -*-
"""Operation methods package."""


def operate(num1, num2, operator):
    """Do operation of the two numbers with sign + or -.
    inputs are only integers"""
    return num1 - num2 if operator == "-" else num1 + num2
