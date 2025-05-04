def solution(people, limit):
    people = sorted(people)
    answer = 0
    length = len(people)
    left = 0
    right = length - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    # left가 right보다 크면 people은 짝 맞춰 나갔고
    # left가 right와 같으면 people은 한 명 남았다
    answer += abs(left-right-1)
    return answer