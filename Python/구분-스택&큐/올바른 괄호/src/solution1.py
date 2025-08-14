def solution(s):
    answer = True
    stack = []
    
    for x in s:
		# 시작의 괄호를 넣는다.
        if x == '(':
            stack.append(x)
        # stack에 시작의 괄호가 있을 때, 끝 괄호가 들어올 시 제거
        elif stack:
            stack.pop()
        # stack에 시작의 괄호가 없을 때, 끝 괄호가 들어올 시 실패
        else:
            return False
    
    # 전부 짝이 맞으면
    if stack:
        answer = False

    return answer