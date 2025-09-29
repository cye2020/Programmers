import pytest
from src.solution1 import solution


@pytest.mark.parametrize("number, expected", [
    (
        'baabaa',
        1
    ),
    (
        'cdcd',
        0
    ),
    (
        'aa',
        1
    )
])
def test_solution(number, expected):
    assert solution(number) == expected