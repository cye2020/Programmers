def get(c, s, n):
    if (c[s-1] == 2) and (s > 0):
        c[s-1] = 1
        c[s] = 1
        return 1
    elif (s < n-1) and (c[s+1] == 2):
        c[s+1] = 1
        c[s] = 1
        return 1
    else:
        return 0

def solution(n, lost, reserve):
    c = [1] * n
    answer = 0
    for x in lost:
        c[x-1] -= 1
    for x in reserve:
        c[x-1] += 1
    for s in range(n):
        if c[s] == 0:
            answer += get(c, s, n)
        else:
            answer += 1
    return answer


if __name__ == "__main__":
    sol = solution(30, [1,2,4,30], [1,4,5])
    print(sol)