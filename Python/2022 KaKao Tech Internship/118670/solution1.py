from typing import Any, List


class Point:
    def __init__(self, number, cord):
        self.number = number
        self.cord = cord
        self.rotate = None
    
    def __iter__(self):
        return self
    
    def right(self):
        self.cord[0] += 1
    
    def down(self):
        self.cord[1] += 1
    
    def left(self):
        self.cord[0] -= 1
    
    def up(self):
        self.cord[1] -= 1



class MatrixOperator:
    def __init__(self, points: List[List[Point]], operations):
        self.points = points
        self.operations = operations
        self.op = {'Rotate': self.rotate, 'ShiftRow': self.shiftrow}
        self.index = 0
        self.m = len(self.points[0])
        self.n = len(self.points)
        
        for k in range(min(self.m, self.n) // 2):
            for q in range(k, self.m - 1 - k):
                point = points[k][q]
                point.rotate = point.right 
            for p in range(k, self.n - 1 - k):
                point = points[p][self.m - 1 - k]
                point.rotate = point.down
            for q in range(self.m - 1 - k, k, -1):
                point = points[self.n - 1 - k][q]
                point.rotate = point.left
            for p in range(self.n - 1 - k, k, -1):
                point = points[p][k]
                point.rotate = point.up

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.op[self.operations[self.index]]()
        self.index += 1
        return self.points
    
    def rotate(self):
        for p in range(self.n):
            for q in range(self.m):
                self.points[p][q].rotate()
    
    def shiftrow(self):
        for p in range(self.n):
            for q in range(self.m):
                point = self.points[p][q]
                if point.cord[1] == self.n - 1:
                    point.cord[1] = 0
                else:
                    point.down()



def solution(rc, operations):
    points = [[Point(element, (i, j)) for j, element in enumerate(row)] for i, row in enumerate(rc)]

    for row in points:
        for element in row:
            print(element.number, end=' ')
    operator = MatrixOperator(points, operations)
    for op in operator:
        print(op)
    answer = [[]]
    return answer


rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
operations = ["Rotate", "ShiftRow"]
print(len(rc), len(rc[0]))
solution(rc, operations)