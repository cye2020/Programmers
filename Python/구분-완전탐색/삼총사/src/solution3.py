from itertools import combinations

def solution(number):
    answer = sum(1 for case in combinations(number, 3) if sum(case) == 0)
    return answer