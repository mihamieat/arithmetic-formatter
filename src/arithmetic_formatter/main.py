# -*- coding: utf-8 -*-
"""Main package."""
# -*- coding: utf-8 -*-
from typing import List

from arithmetic_formatter.myoperate import operate
from arithmetic_formatter.myparse import parse_operation
from arithmetic_formatter.format import (
    first_line,
    second_line,
    result_line,
    number_of_dashes,
    display_dashes,
)

SPACES_BETWEEN_OPS = 4


def arithmetic_arranger(operations: List[str], resolve: bool = False) -> str:
    """Arithmetic arranger function."""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    if len(operations) > 5:
        return "Error: Too many problems."
    for operation in operations:
        try:
            first_num, second_num, operator = parse_operation(operation)
        except ValueError:
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if len(str(first_num)) > 4 or len(str(second_num)) > 4:
            return "Error: Numbers cannot be more than four digits."
        result = operate(first_num, second_num, operator)
        nr_of_dashes = number_of_dashes(str(first_num), str(second_num))

        line1 += first_line(nr_of_dashes, str(first_num)) + " " * SPACES_BETWEEN_OPS
        line2 += (
            second_line(nr_of_dashes, str(second_num), operator)
            + " " * SPACES_BETWEEN_OPS
        )
        line3 += display_dashes(nr_of_dashes) + " " * SPACES_BETWEEN_OPS
        line4 += result_line(nr_of_dashes, str(result)) + " " * SPACES_BETWEEN_OPS
    return (
        line1.rstrip()
        + "\n"
        + line2.rstrip()
        + "\n"
        + line3.rstrip()
        + "\n"
        + line4.rstrip()
        if resolve
        else line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    )


if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    print(
        arithmetic_arranger(
            ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True
        )
    )
    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
