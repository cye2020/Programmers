import pytest
# from src.solution1 import solution
from src.solution2 import solution


@pytest.mark.parametrize("n, costs, result", [
    (
        4,
        [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]],
        4
    ), 
])
def test_solution(n, costs, result):
    assert solution(n, costs) == result