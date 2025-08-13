import pytest
from src.solution1 import solution


@pytest.mark.parametrize("num1, num2, expected_output", [
    (
        3,
        4,
        12
    ),
    (
        27,
        19,
        513
    ),
])
def test_solution(num1, num2, expected_output):
    assert solution(num1, num2) == expected_output