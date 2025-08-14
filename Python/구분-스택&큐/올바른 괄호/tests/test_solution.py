import pytest
from src.solution1 import solution as solution1
from src.solution2 import solution as solution2


@pytest.mark.parametrize("s, result", [
    (
        "()()",
        True
    ),
    (
        "(())()",
        True
    ),
    (
        ")()(",
        False
    ),
    (
        "(()(",
        False
    ),
])
def test_solution(s, result):
    assert solution1(s) == result
    assert solution2(s) == result