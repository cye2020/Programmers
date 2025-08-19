import pytest
from src.solution1 import solution as solution1


@pytest.mark.parametrize("s, result", [
    (
        "3people unFollowed me",
        "3people Unfollowed Me"
    ),
    (
        "for the last week",
        "For The Last Week"
    ),
])
def test_solution(s, result):
    assert solution1(s) == result