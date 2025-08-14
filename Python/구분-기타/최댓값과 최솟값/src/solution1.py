def solution(s):
    numbers = list(map(int, s.split()))
    answer = f'{min(numbers)} {max(numbers)}'
    return answer