import pytest
from src.solution1 import solution


@pytest.mark.parametrize("number, expected", [
    (
        78,
        83
    ),
    (
        15,
        23
    ),
])
def test_solution(number, expected):
    assert solution(number) == expected