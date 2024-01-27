import pytest
from arithmetic_formatter.myparse import parse_operation

# Happy path tests with various realistic test values
@pytest.mark.parametrize("operation_string, expected", [
    ("3 + 7", (3, 7, '+')), # ID: test_addition
    ("10 - 2", (10, 2, '-')), # ID: test_subtraction
    ("8 * 3", (8, 3, '*')), # ID: test_multiplication
    ("20 / 4", (20, 4, '/')), # ID: test_division
], ids=["test_addition", "test_subtraction", "test_multiplication", "test_division"])
def test_parse_operation_happy_path(operation_string, expected):
    # Act
    result = parse_operation(operation_string)
    
    # Assert
    assert result == expected

# Edge cases
@pytest.mark.parametrize("operation_string, expected", [
    ("0 + 0", (0, 0, '+')), # ID: test_zero_addition
    ("-1 - -1", (-1, -1, '-')), # ID: test_negative_numbers
    ("9999999 * 1", (9999999, 1, '*')), # ID: test_large_numbers
], ids=["test_zero_addition", "test_negative_numbers", "test_large_numbers"])
def test_parse_operation_edge_cases(operation_string, expected):
    # Act
    result = parse_operation(operation_string)
    
    # Assert
    assert result == expected

# Error cases
# @pytest.mark.parametrize("operation_string, expected_exception", [
#     ("3 +", ValueError), # ID: test_missing_operand
#     ("+ 7", ValueError), # ID: test_leading_operator
#     ("3 7", ValueError), # ID: test_missing_operator
#     ("three + seven", ValueError), # ID: test_non_numeric_operands
#     ("3 ++ 7", ValueError), # ID: test_double_operator
#     ("3 + 7 10", ValueError), # ID: test_extra_operand
# ], ids=["test_missing_operand", "test_leading_operator", "test_missing_operator", "test_non_numeric_operands", "test_double_operator", "test_extra_operand"])
# def test_parse_operation_error_cases(operation_string, expected_exception):
#     # Act & Assert
#     with pytest.raises(expected_exception):
#         parse_operation(operation_string)
