def solution(s):
    answer = ''
    prev = ' '
    for char in s:
        if prev == ' ' and char != ' ':
            answer += char.upper()
        else:
            answer += char.lower()
        prev = char
    return answer