from collections import deque
import math

def get_time(progresses, speeds, i):
    left = 100 - progresses[i]
    speed = speeds[i]
    t = math.ceil(left / speed)
    return t

def solution(progresses, speeds):
    answer = []
    l = len(speeds)
    max_t = get_time(progresses, speeds, 0)
    cnt = 1
    for i in range(1, l):
        t = get_time(progresses, speeds, i)
        if t <= max_t:
            cnt += 1
        else:
            answer.append(cnt)
            max_t = t
            cnt = 1
    answer.append(cnt)
    return answer