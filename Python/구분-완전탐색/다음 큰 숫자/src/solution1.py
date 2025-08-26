def solution(n):
    answer = n + 1
    cnt1 = bin(n).count('1')
    while bin(answer).count('1') != cnt1:
        answer += 1
    return answer