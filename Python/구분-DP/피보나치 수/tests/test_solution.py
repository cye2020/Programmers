import pytest
from src.solution1 import solution


@pytest.mark.parametrize("N, number, expected_output", [
    (
        3,
        2
    ),
    (
        5,
        5
    ),
    (
        100000,
        1168141
    )
])
def test_solution(N, number, expected_output):
    assert solution(N, number) == expected_output