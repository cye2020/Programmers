def solution(s):
    # 짝을 기다리는 페어 개수
    pair = 0
    
    for x in s:
		# 시작 괄호가 들어오면 +1, 끝 괄호가 들어오면 -1
        pair = pair + 1 if x == '(' else pair -1
        # 시작 괄호도 없는데 끝 괄호가 들어오면 이미 오답
        if pair < 0:
            break
		# 모두가 짝이 있다면
    answer = pair == 0
    return answer