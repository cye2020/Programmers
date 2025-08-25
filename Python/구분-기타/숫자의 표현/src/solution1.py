def solution(n):
    answer = 0
    for m in range(1, n+1):
        q = n // m
        r = n % m
        if q <= (m+1) // 2 - 1:
            break
        else:
            if (m % 2 == 0) and r == m // 2:
                answer += 1
            elif (m % 2 == 1) and r == 0:
                answer += 1
            else:
                pass
    return answer