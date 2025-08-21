import pytest
from src.solution1 import solution as solution1


@pytest.mark.parametrize("s, result", [
    (
        "110010101001",
        [3,8]
    ),
    (
        "01110",
        [3,3]
    ),
    (
        "1111111",
        [4,1]
    ),
])
def test_solution(s, result):
    assert solution1(s) == result