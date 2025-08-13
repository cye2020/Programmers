import pytest
from src.solution1 import solution


@pytest.mark.parametrize("age, expected_output", [
    (
        40,
        1983
    ),
    (
        23,
        2000
    ),
])
def test_solution(age, expected_output):
    assert solution(age) == expected_output