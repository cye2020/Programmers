class Line:
    def __init__(self, n):
        self.n = n
        self.top = -1
        self.dolls = []

    def add(self, doll):
        self.dolls.append(doll)
        self.top += 1
    
    def pop(self):
        if self.top == -1:
            return 0
        doll = self.dolls[self.top]
        self.top -= 1
        return doll

def solution(board, moves):
    stack = []
    answer = 0
    N = len(board)
    M = len(board[0])
    lines = [Line(i) for i in range(M)]
    for i in range(N):
        for j in range(M):
            if board[N-i-1][j] != 0:
                lines[j].add(board[N-i-1][j])

    for x in moves:
        doll = lines[x-1].pop()
        if doll == 0:
            continue
        stack.append(doll)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer