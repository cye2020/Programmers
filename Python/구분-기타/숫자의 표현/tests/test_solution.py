import pytest
from src.solution1 import solution


@pytest.mark.parametrize("n, answer", [
    (
        15,
        4
    ),
    (
        1,
        1
    ),
])
def test_solution(n, answer):
    assert solution(n) == answer