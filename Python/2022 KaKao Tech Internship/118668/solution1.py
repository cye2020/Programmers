class Problem:
    def __init__(self, alp_req, cop_req, alp_rwd, cop_rwd, cost) -> None:
        self.alp_req = alp_req
        self.cop_req = cop_req
        self.alp_rwd = alp_rwd
        self.cop_rwd = cop_rwd
        self.cost = cost

def solution(alp, cop, problems):
    max_alp_req = 0
    max_cop_req = 0
    for i in range(len(problems)):
        p = Problem(*problems[i])
        problems[i] = p
        max_alp_req = max(p.alp_req - alp, max_alp_req)
        max_cop_req = max(p.cop_req - cop, max_cop_req)
    
    DP = [[i+j for i in range(max_cop_req + 1)] for j in range(max_alp_req + 1)]
    problems.append(Problem(0, 0, 1, 0, 1))
    problems.append(Problem(0, 0, 0, 1, 1))
    
    for i in range(max_alp_req + 1):
        for j in range(max_cop_req + 1):
            for p in problems:
                if (alp + i >= p.alp_req) and (cop + j >= p.cop_req):
                    next_i = min(i+p.alp_rwd, max_alp_req)
                    next_j = min(j+p.cop_rwd, max_cop_req)
                    DP[next_i][next_j] = min(DP[i][j] + p.cost, DP[next_i][next_j])
    answer = DP[max_alp_req][max_cop_req]
    return answer


Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 100],
        [0, 0, 2, 2, 1],
    ],
}

print(Q4["problems"])
answer = solution(**Q4)
print(answer)