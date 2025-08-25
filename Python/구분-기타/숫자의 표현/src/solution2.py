def solution(n):
    answer = 0
    r_max = int((n*2 + 1)**0.5) + 1
    for m in range(1, r_max):
        q = n // m
        r = n % m
        if (m % 2 == 0) and r == m // 2:
            answer += 1
        elif (m % 2 == 1) and r == 0:
            answer += 1
        else:
            pass
    return answer