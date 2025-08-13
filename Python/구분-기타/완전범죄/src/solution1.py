def solution(info, n, m):
    DP = [[False for _ in range(m)] for _ in range(n)]
    DP[0][0] = True
    
    for tA, tB in info:
        new_DP = [[False for _ in range(m)] for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if not DP[a][b]:
                    continue
                if a + tA < n:
                    new_DP[a+tA][b] = True
                if b + tB < m:
                    new_DP[a][b+tB] = True
        del DP
        DP = new_DP
    for i in range(n):
        for j in range(m):
            if DP[i][j]:
                return i
    return -1