def solution(n):
    answer = 0
    DP = [[] for _ in range(n+1)]
    DP[1] = [1]
    for i in range(2, (n+1)//2 + 1):
        DP[i].append(i)
        for x in DP[i-1]:
            if x + i == n:
                answer += 1
            elif x + i > n:
                break
            DP[i].append(x+i)
    answer += 1
    return answer