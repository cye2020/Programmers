import pytest
from src.solution1 import solution


@pytest.mark.parametrize("participant, completion, expected_output", [
    (
        ["leo", "kiki", "eden"],
        ["eden", "kiki"],
        "leo"
    ),
    (
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
        "vinko"
    ),
    (
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "ana", "mislav"],
        "mislav"
    )  
])
def test_solution(participant, completion, expected_output):
    assert solution(participant, completion) == expected_output