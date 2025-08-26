import pytest
from src.solution1 import solution


@pytest.mark.parametrize("number, expected", [
    (
        [-2, 3, 0, 2, -5],
        2
    ),
    (
        [-3, -2, -1, 0, 1, 2, 3],
        5
    ),
    (
        [-1, 1, -1, 1],
        0
    )
])
def test_solution(number, expected):
    assert solution(number) == expected