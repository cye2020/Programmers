# 크루스칼 알고리즘

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

def kruskal(n, costs):
    ds = DisjointSet(n)
    total_cost = 0
    costs = sorted(costs, key=lambda x: x[2])
    for a, b, cost in costs:
        if ds.union(a, b):
            total_cost += cost
    return total_cost


def solution(n, costs):
    answer = kruskal(n, costs)
    return answer