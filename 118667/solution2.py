def solution(queue1, queue2):
    queue = queue1 + queue2
    
    now = sum(queue1)
    target = now + sum(queue2)
    
    if target % 2 == 1:
        return -1
    else:
        target //= 2
    
    q1 = len(queue1)
    t = len(queue)
    i = 0
    j = q1
    
    
    for cnt in range(t + max(q1, t-q1)):
        if now == target:
            return cnt

        if now > target:
            n = queue[i]
            i = (i + 1) % t
            now -= n

        elif now < target:
            n = queue[j]
            j = (j + 1) % (t)
            now += n
        
        if n > target:
            return -1
    return -1


if __name__ == '__main__':
    queue1 = [1, 1, 1, 8, 10, 9]
    queue2 = [1, 1, 1, 1, 1, 1]
    
    print(solution(queue1, queue2))