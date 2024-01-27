import pytest
from arithmetic_formatter.myoperate import operate

# Happy path tests with various realistic test values
@pytest.mark.parametrize("num1, num2, operator, expected", [
    (1, 1, '+', 2),  # ID: AddPositive
    (1, 1, '-', 0),  # ID: SubtractPositive
    (-1, -1, '+', -2),  # ID: AddNegative
    (-1, -1, '-', 0),  # ID: SubtractNegative
    (0, 0, '+', 0),  # ID: AddZero
    (0, 0, '-', 0),  # ID: SubtractZero
    (1000, 1, '+', 1001),  # ID: AddLargeNumber
    (1000, 1, '-', 999),  # ID: SubtractLargeNumber
])
def test_operate_happy_path(num1, num2, operator, expected):
    # Act
    result = operate(num1, num2, operator)

    # Assert
    assert result == expected, f"Expected {expected}, got {result}"

# Edge cases
# @pytest.mark.parametrize("num1, num2, operator, expected", [
#     (1, 0, '+', 1),  # ID: AddWithZero
#     (0, 1, '-', -1),  # ID: SubtractFromZero
#     (1, -1, '+', 0),  # ID: AddWithNegative
#     (-1, 1, '-', -2),  # ID: SubtractWithNegative
#     (1, 1, ' ', None),  # ID: InvalidOperatorSpace
#     (1, 1, '*', None),  # ID: InvalidOperatorAsterisk
# ])
# def test_operate_edge_cases(num1, num2, operator, expected):
#     # Act
#     result = operate(num1, num2, operator)

#     # Assert
# # sourcery skip: no-conditionals-in-tests
#     if operator not in ['+', '-']:
#         with pytest.raises(ValueError):
#             operate(num1, num2, operator)
#     else:
#         assert result == expected, f"Expected {expected}, got {result}"

# Error cases
# @pytest.mark.parametrize("num1, num2, operator, expected_exception", [
#     ('a', 1, '+', TypeError),  # ID: NonIntegerFirstArgument
#     (1, 'b', '+', TypeError),  # ID: NonIntegerSecondArgument
#     (1.0, 1, '+', TypeError),  # ID: FloatFirstArgument
#     (1, 1.0, '+', TypeError),  # ID: FloatSecondArgument
# ])
# def test_operate_error_cases(num1, num2, operator, expected_exception):
#     # Act and Assert
#     with pytest.raises(expected_exception):
#         operate(num1, num2, operator)
