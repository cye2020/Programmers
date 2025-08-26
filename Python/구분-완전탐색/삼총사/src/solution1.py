def solution(number):
    answer = 0
    len_n = len(number)
    for i in range(len_n - 2):
        for j in range(i+1, len_n - 1):
            for k in range(j+1, len_n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer