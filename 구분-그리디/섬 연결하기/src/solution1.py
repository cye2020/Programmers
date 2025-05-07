
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    islands = [[False] * n for _ in range(n)]
    for i in range(n):
        islands[i][i] = True
    
    for cost in costs:
        a, b, c = cost
        if islands[a][b] == False:
            for i in range(n):
                if islands[a][i] == True:
                    for j in range(n):
                        if islands[b][j] == True:
                            islands[i][j] = True
                            islands[j][i] = True
            answer += c
            # print(cost)
            # print(islands)
    return answer