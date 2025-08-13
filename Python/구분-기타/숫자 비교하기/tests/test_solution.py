import pytest
from src.solution1 import solution


@pytest.mark.parametrize("num1, num2, expected_output", [
    (
        2,
        3,
        -1
    ),
    (
        11,
        11,
        1
    ),
    (
        7,
        99,
        -1
    )
])
def test_solution(num1, num2, expected_output):
    assert solution(num1, num2) == expected_output