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
        problem = Problem(*problems[i])
        problems[i] = problem
        max_alp_req = max(problem.alp_req - alp, max_alp_req)
        max_cop_req = max(problem.cop_req - cop, max_cop_req)
    
    DP = [[i+j for i in range(max_cop_req + 1)] for j in range(max_alp_req + 1)]
    problems.append(Problem(0, 0, 1, 0, 1))
    problems.append(Problem(0, 0, 0, 1, 1))
    
    for i in range(max_alp_req + 1):
        for j in range(max_cop_req + 1):
            for problem in problems:
                alp_req = problem[0]
                cop_req = problem[1]
                if (alp + i >= alp_req) and (cop + j >= cop_req):
                    alp_rwd = problem[2]
                    cop_rwd = problem[3]
                    cost = problem[4]
                    next_i = min(i+alp_rwd, max_alp_req)
                    next_j = min(j+cop_rwd, max_cop_req)
                    DP[next_i][next_j] = min(DP[i][j] + cost, DP[next_i][next_j])
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
answer = solution(*Q4.values())
print(answer)