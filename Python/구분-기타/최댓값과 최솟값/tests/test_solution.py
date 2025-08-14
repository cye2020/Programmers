import pytest
from src.solution1 import solution


@pytest.mark.parametrize("s, result", [
    (
        "1 2 3 4",
        "1 4"
    ),
    (
        "-1 -2 -3 -4",
        "-4 -1"
    ),
    (
        "-1 -1",
        "-1 -1"
    )
])
def test_solution(s, result):
    assert solution(s) == result