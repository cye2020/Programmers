def solution(answers):
    N = len(answers)
    # 수포자 1, 2, 3의 답안
    s1_pattern = [1, 2, 3, 4, 5]
    s2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    s3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1 = s1_pattern * (N//5) + s1_pattern[:N % 5]
    s2 = s2_pattern * (N // 8) + s2_pattern[:N % 8]
    s3 = s3_pattern * (N // 10) + s3_pattern[:N % 10]

    # 각 수포자의 정답 개수
    s1_count = sum([x==y for x, y in zip(s1, answers)])
    s2_count = sum([x==y for x, y in zip(s2, answers)])
    s3_count = sum([x==y for x, y in zip(s3, answers)])
    
    # 가장 많이 맞춘 수포자 찾기
    max_count = max(s1_count, s2_count, s3_count)
    answer = sorted([i+1 for i in range(3) if [s1_count, s2_count, s3_count][i] == max_count])
    return answer


if __name__ == '__main__':
    # 테스트 케이스
    answers = [1, 2, 3, 4, 5, 6]
    answer = solution(answers)
    print(answer)