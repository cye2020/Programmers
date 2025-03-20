class Dart:
    def __init__(self, turn):
        self.turn = turn
        self.result = [{"score": None, "bonus": None, "option": None, "final": None} for _ in range(turn)]
        self.bonus = {"S": 1, "D": 2, "T": 3}
    def record(self, result):
        turn = -1
        for i, x in enumerate(result):
            if x.isdigit():
                if i > 0 and result[i-1].isdigit():
                    self.result[turn]["score"] += x
                    continue
                turn += 1
                self.result[turn]["score"] = x
            elif x in ["S", "D", "T"]:
                self.result[turn]["bonus"] = x
            else:
                self.result[turn]["option"] = x
    def calculate(self):
        for i in range(self.turn):
            result = self.result[i]
            score = int(result["score"])
            bonus = self.bonus[result["bonus"]]
            option = result["option"]
            final = score**bonus
            if option == "*":
                self.result[i]["final"] = 2*final
                if i > 0:
                    self.result[i-1]["final"] *= 2
            elif option == "#":
                self.result[i]["final"] = -1 * final
            else:
                self.result[i]["final"] = final
    def sum(self):
        ret = sum([item["final"] for item in self.result])
        return ret
            
def solution(dartResult):
    dart = Dart(3)
    dart.record(dartResult)
    dart.calculate()
    answer = dart.sum()
    return answer