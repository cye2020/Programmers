def solution(s):
    lst = []
    for word in s.lower().split():
        nword = list(word)
        nword[0] = nword[0].upper()
        lst.append(''.join(nword))
    answer = ' '.join(lst)
    return answer