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

spaces_between_ops = 4


def arithmetic_arranger(operations: List[str]):
    """Arithmetic arranger function."""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for operation in operations:
        first_num, second_num, operator = parse_operation(operation)
        result = operate(first_num, second_num, operator)
        nr_of_dashes = number_of_dashes(str(first_num), str(second_num), str(result))

        line1 += first_line(nr_of_dashes, str(first_num)) + " " * spaces_between_ops
        line2 += (
            second_line(nr_of_dashes, str(second_num), operator)
            + " " * spaces_between_ops
        )
        line3 += display_dashes(nr_of_dashes) + " " * spaces_between_ops
        line4 += result_line(nr_of_dashes, str(result)) + " " * spaces_between_ops
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4


if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
