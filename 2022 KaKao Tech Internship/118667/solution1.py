# 두 수의 합의 절반이 넘는 숫자가 있으면 return -1
from collections import deque


def solution(queue1, queue2):
    now = sum(queue1)
    target = now + sum(queue2)
    
    if target % 2 == 1:
        return -1
    else:
        target //= 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    
    for _ in range(600000):
        if now == target:
            return answer
        
        # queue1 -> queue2
        if now > target:
            n = queue1.popleft()
            queue2.append(n)
            now -= n
            answer += 1
        
        # queue2 -> queue1
        if now < target:
            n = queue2.popleft()
            queue1.append(n)
            now += n
            answer += 1

        if n > target:
            return -1
    return -1


if __name__ == '__main__':
    queue1 = [1, 1, 1, 8, 10, 9]
    queue2 = [1, 1, 1, 1, 1, 1]
    
    print(solution(queue1, queue2))