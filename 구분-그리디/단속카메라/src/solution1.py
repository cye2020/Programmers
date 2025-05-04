from collections import defaultdict
from copy import deepcopy

class Gate:
    def __init__(self, idx):
        self.idx = idx
        self.cars = set()
        self.num = 0
    
    def add(self, car):
        self.cars.add(car)
        self.num += 1
    
    def remove(self, car):
        self.cars.remove(car)
        self.num -= 1
    
    def __lt__(self, other):
        return self.num < other.num

class GateDict(dict):
    def __missing__(self, key):
        self[key] = Gate(key)
        return self[key]

def solution(routes):
    for i, route in enumerate(routes):
        gatein = min(route[0], route[1])
        gateout = max(route[0], route[1])
        routes[i] = list(range(gatein, gateout + 1))
    gates = GateDict()
    cars = defaultdict(list)
    for i, route in enumerate(routes):
        for g in route:
            gate = gates[g]
            gate.add(i)
            cars[i].append(gate)

    capture = []
    answer = 0
    while len(capture) < len(routes):
        gates_cp = deepcopy(gates)
        gates_list = sorted(gates_cp.values(), reverse=True)
        gate: Gate = gates_list[0]
        capture.extend(gate.cars)
        for car in gate.cars:
            for g in cars[car]:
                g.remove(car)
        # print(f"capture: {capture}")
        answer += 1
    return answer