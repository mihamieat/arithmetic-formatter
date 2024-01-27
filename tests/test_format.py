import pytest
from src.arithmetic_formatter.format import display_line, second_line

# Happy path tests with various realistic test values
@pytest.mark.parametrize("line, space, expected_output, test_id", [
    (["Hello"], 0, "Hello", "test_no_space_single_word"),
    (["Hello", "World"], 0, "Hello", "test_no_space_two_words"),
    (["Hello"], 5, "     Hello", "test_with_space_single_word"),
    (["123", "456"], 3, "   123", "test_with_space_numbers"),
    ([""], 0, "", "test_no_space_empty_string"),
    (["Hello", "World"], 10, "          Hello", "test_large_space_two_words"),
])
def test_display_line_happy_path(line, space, expected_output, test_id):
    
    # Act
    result = display_line(line, space)

    # Assert
    assert result == expected_output, f"Failed {test_id}"

# Edge cases
@pytest.mark.parametrize("line, space, expected_output, test_id", [
    ([""], 10, "          ", "test_space_with_empty_string"),
    (["Hello", "World", "!"], 1, " Hello", "test_space_with_multiple_words"),
    (["\tHello", "\tWorld"], 0, "\tHello", "test_tab_character_in_line"),
    (["Hello\nWorld"], 0, "Hello\nWorld", "test_newline_character_in_line"),
])
def test_display_line_edge_cases(line, space, expected_output, test_id):
    
    # Act
    result = display_line(line, space)

    # Assert
    assert result == expected_output, f"Failed {test_id}"

# Error cases
# @pytest.mark.parametrize("line, space, expected_exception, test_id", [
#     ([None], 0, TypeError, "test_none_in_line"),
#     (["Hello", 123], 0, TypeError, "test_non_string_in_line"),
#     (["Hello"], "two", TypeError, "test_non_integer_space"),
#     (["Hello"], -1, ValueError, "test_negative_space"),
# ])
# def test_display_line_error_cases(line, space, expected_exception, test_id):
    
#     # Act and Assert
#     with pytest.raises(expected_exception):
#         display_line(line, space)


# Happy path tests with various realistic test values
@pytest.mark.parametrize("number_of_dashes, num2, operator, expected", [
    pytest.param(5, "2", "+", "+   2", id="happy-path-plus-short-num"),
    pytest.param(6, "12", "-", "-   12", id="happy-path-minus-normal-num"),
    pytest.param(8, "123", "*", "*    123", id="happy-path-multiply-long-num"),
    pytest.param(7, "0", "/", "/     0", id="happy-path-divide-zero"),
], ids=str)
def test_second_line_happy_path(number_of_dashes, num2, operator, expected):
    # Act
    result = second_line(number_of_dashes, num2, operator)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

# Edge cases
@pytest.mark.parametrize("number_of_dashes, num2, operator, expected", [
    pytest.param(4, "1", "+", "+  1", id="edge-case-exact-fit"),
    pytest.param(5, "10", "-", "-  10", id="edge-case-no-space"),
], ids=str)
def test_second_line_edge_cases(number_of_dashes, num2, operator, expected):
    # Act
    result = second_line(number_of_dashes, num2, operator)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

# # Error cases
# @pytest.mark.parametrize("number_of_dashes, num2, operator", [
#     pytest.param(3, "100", "+", id="error-case-too-many-digits"),
#     pytest.param(5, "abc", "-", id="error-case-non-numeric-second-argument"),
#     pytest.param(5, "2", "++", id="error-case-invalid-operator"),
#     pytest.param(0, "2", "-", id="error-case-no-dashes"),
# ], ids=str)
# def test_second_line_error_cases(number_of_dashes, num2, operator):
#     # Act
#     with pytest.raises(ValueError) as exc_info:
#         second_line(number_of_dashes, num2, operator)

#     # Assert
#     assert str(exc_info.value), "An error should have been raised for invalid input"
