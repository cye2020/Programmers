def solution(name: str) -> int:
    answer = 0
    rem = 0
    cnt = float('inf')  # Integer.MAX_VALUE 대신 파이썬에서는 float('inf') 사용

    for i in range(len(name)):
        if name[i] != 'A':
            answer += calc(name[i])

            if i == 0:
                continue

            tmp = rem + len(name) - i
            print(f"rem: {rem}, tmp: {tmp}, len-i: {len(name)-i}")
            print(cnt, tmp + rem, tmp + len(name) - i)
            cnt = min(cnt, min(tmp + rem, tmp + len(name) - i))
            rem = i
            # print(tmp, cnt, rem)

    print(f"rem: {rem}, cnt: {cnt}")
    cnt = min(rem, cnt)
    return answer + cnt

def calc(c: str) -> int:
    cint = ord(c)  # 파이썬에서는 char의 아스키 값을 구할 때 ord() 사용
    return min(91 - cint, cint - 65)



# Test
# print(solution("BBAB"))
print(solution("")) # 15






distance = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
    "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13,
    "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7,
    "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1
}

def compare(name, word, cur, length):
    left = -1
    right = -1
    for i in range(length):
        right_index = (cur + i) % length
        left_index = (cur - i) % length
        if (name[right_index] == word[right_index]):
            right += 1
        else:
            return True, right + 1
        if (name[left_index] == word[left_index]):
            left += 1
        else:
            return False, left + 1

def solution(name):
    length = len(name)
    name_list = list(name)
    word_list = ["A"] * length
    cur = 0
    answer = 0
    while (word_list != name_list):
        dir, step = compare(name_list, word_list, cur, length)
        print(dir, step)
        if dir:
            cur += step
        else:
            cur = (cur - step) % length
        answer += (distance[name_list[cur]] + step)
        word_list[cur] = name_list[cur]
        print(answer)
        print(word_list, name_list)
        
    return answer