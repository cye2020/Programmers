import pytest
from src.solution1 import solution


@pytest.mark.parametrize("board, moves, result", [
    (
        [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
        [1,5,3,5,1,2,1,4],
        4
    ), 
])
def test_solution(board, moves, result):
    assert solution(board, moves) == result