def solution(participant, completion):
    if set(participant) != set(completion):
        answer = list(set(participant) - set(completion)).pop()
    else:
        participant = sorted(participant)
        completion = sorted(completion)
        for i in range(len(participant)):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
    return answer