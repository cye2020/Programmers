from collections import Counter
import re

def solution(s):
    gen = map(int, re.findall('\\d+', s))
    cnt = Counter(gen)
    answer = [t[0] for t in cnt.most_common()]
    return answer