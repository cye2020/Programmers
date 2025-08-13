import pytest
from src.solution1 import solution


@pytest.mark.parametrize("num1, num2, expected_output", [
    (
        2,
        3,
        5
    ),
    (
        100,
        2,
        102
    ),
])
def test_solution(num1, num2, expected_output):
    assert solution(num1, num2) == expected_output