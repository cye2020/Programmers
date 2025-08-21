# 남의 풀이
def solution(s):
    answer = ''
    capitalized = list(map(lambda x:x.capitalize(), s.split(' ')))
    # capitalized = [x.capitalize() for x in s.split()]
    answer = " ".join(capitalized)
    
    return answer