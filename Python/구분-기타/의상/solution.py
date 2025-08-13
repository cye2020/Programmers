from collections import defaultdict

def solution(clothes):
    hash = defaultdict(int)
    for l in clothes:
        hash[l[1]] += 1
    answer = 1
    for v in hash.values():
        answer *= (v+1)
    answer -= 1
    return answer