def solution(number, k):
    keep = len(number) - k
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    answer = ''.join(stack[:keep])
    return answer


if __name__ == '__main__':
    number = "991999199"
    k = 5
    number = "1924"
    k = 2
    print(solution(number, k))