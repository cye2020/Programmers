import pytest
from src.solution1 import solution


@pytest.mark.parametrize("numbers, hand, result", [
    (
        3,
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
        50
    ),
    (
        3,
        ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
        21
    ), 
    (
        2,
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        60
    ), 
    (
        5,
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        52
    ),
    (
        2,
        ["Jeju", "Pangyo", "NewYork", "newyork"],
        16
    ),
    (
        0,
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
        25
    )
])
def test_solution(numbers, hand, result):
    assert solution(numbers, hand) == result