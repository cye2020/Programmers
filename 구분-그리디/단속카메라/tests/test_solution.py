import pytest
from src.solution1 import solution1
from src.solution2 import solution2


@pytest.mark.parametrize("routes, result", [
    (
        [[-20,-15], [-14,-5], [-18,-13], [-5,-3]],
        2
    ), 
])
def test_solution(routes, result):
    # assert solution1(routes) == result
    assert solution2(routes) == result