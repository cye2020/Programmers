from itertools import permutations

class Dungeon:
    def __init__(self, need, use):
        self.need = need
        self.use = use
    def __gt__(self, other):
        return [self.use, self.need] > [other.use, other.need]
    def __str__(self):
        return f"need: {self.need}, use: {self.use}"

class User:
    def __init__(self, k):
        self.k = k
    def explore(self, dungeon: Dungeon):
        if self.k >= dungeon.need:
            self.k -= dungeon.use
            return True
        else:
            return False


def solution(k, dungeons):
    answer = 0
    dungeons = [Dungeon(*x) for x in dungeons]
    for per in permutations(dungeons):
        user = User(k)
        success = 0
        for dungeon in per:
            if user.explore(dungeon):
                success += 1 
        answer = max(answer, success)
        del user
    return answer