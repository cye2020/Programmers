import pytest
from src.solution1 import solution


@pytest.mark.parametrize("N, number, expected_output", [
    (
        5,
        12,
        4
    ),
    (
        2,
        11,
        3
    ),
])
def test_solution(N, number, expected_output):
    assert solution(N, number) == expected_output