from collections import deque

def dfs(n, computers, visited, root):
    stack = deque([root])
    flag = False
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            flag = True
            for i in range(n):
                if (computers[node][i] == 1) and (visited[i] == 0):
                    stack.append(i)
    return flag
    

def bfs(n, computers, visited, root):
    queue = deque([root])
    flag = False
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = 1
            flag = True
            for i in range(n):
                if (computers[node][i] == 1) and (visited[i] == 0):
                    queue.append(i)
    return flag
                    
                
def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        cnt = dfs(n, computers, visited, i)
        if cnt > 0:
            answer += 1
    return answer