import pytest
from src.solution1 import solution


@pytest.mark.parametrize("A, B, result", [
    (
        [1, 4, 2],
        [5, 4, 4],
        29
    ),
    (
        [1,2],
        [3,4],
        10
    ),
])
def test_solution(A, B, result):
    assert solution(A, B) == result