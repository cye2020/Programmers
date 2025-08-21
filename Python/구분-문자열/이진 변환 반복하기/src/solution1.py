
from typing import Tuple

def count01_v1(s: str) -> Tuple[int, int]:
    cnt0 = 0
    for i in range(len(s)):
        if s[i] == '0':
            cnt0 += 1
    cnt1 = i + 1 - cnt0
    return cnt0, cnt1

def count01_v2(s: str) -> Tuple[int, int]:
    cnt0 = s.count('0')
    cnt1 = len(s) - cnt0
    return cnt0, cnt1

def count01_v3(s: str) -> Tuple[int, int]:
    cnt1 = sum(map(int, s))
    cnt0 = len(s) - cnt1
    return cnt0, cnt1

def count01_v4(s: str) -> Tuple[int, int]:
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    return cnt0, cnt1

def count01_v5(s: str) -> Tuple[int, int]:
    cnt0 = 0
    cnt1 = 0
    for n in s:
        if n == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    print(cnt0, cnt1)
    return cnt0, cnt1


def solution(s: str):
    sum0 = 0
    cnt = 0
    while s != '1':
        cnt0, cnt1 = count01_v1(s)
        s = bin(cnt1)[2:]
        sum0 += cnt0
        cnt += 1
    answer = [cnt, sum0]
    return answer