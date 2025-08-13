def solution(N, number):
    answer = -1
    DP = [set() for _ in range(9)]
    for i in range(1, 9):
        DP[i].add(int(str(N) * i))
    for i in range(2, 9):
        for j in range(1, i):
            for x1 in DP[j]:
                for x2 in DP[i-j]:
                    DP[i].add(x1 + x2)
                    DP[i].add(x1 * x2)
                    big = max(x1, x2)
                    small = min(x1, x2)
                    if x1 != x2:
                        DP[i].add(big - small)
                    if big % small == 0:
                        DP[i].add(big // small)
    for i in range(1, 9):
        if number in DP[i]:
            answer = i
            break
    return answer


# solution(5, 12)