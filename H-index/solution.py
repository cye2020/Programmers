def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations, reverse=True)
    for i in range(n-1):
        print(i+1, citations[i])
        condition1 = citations[i] >= i+1
        condition2 = citations[i+1] <= i+1
        if condition1 and condition2:
            answer = i+1
            break
    if citations[-1] >= n:
        answer = len(citations)
    return answer
