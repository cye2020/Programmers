import heapq


class Point(object):
    """
    산의 지점
    type:
        gate: 0, summit: 1, rest: 2
    """
    def __init__(self, type):
        super(Point, self).__init__()
        self.type = type
        self.path = []


def dijkstra(points, gates):
    intensities = {point: float('inf') for point in points}
    visited = {point: False for point in points}
    priority_queue = []
    for gate in gates:
        intensities[points[gate-1]] = 0
        priority_queue.append((0, gate))

    while priority_queue:
        current_intensity, curr_p = heapq.heappop(priority_queue)
        # print(curr_p)
        current_point = points[curr_p-1]
        visited[current_point] = True
        
        if current_intensity > intensities[current_point]:
            continue

        for p, t in current_point.path:
            next_intensity = max(current_intensity, t)
            next_point = points[p-1]
            # print(f'next: {p}')
            if (visited[next_point] is True) or (next_point.type == 0):
                continue

            if next_point.type == 1:
                # print(f"next intensity: {next_intensity}")
                # print(f'compare: {intensities[next_point]}')
                intensities[next_point] = min(next_intensity, intensities[next_point])
                continue
            
            else:
                if next_intensity < intensities[next_point]:
                    intensities[next_point] = next_intensity
                    heapq.heappush(priority_queue, (next_intensity, p))

    return intensities


        
def solution(n, paths, gates, summits):
    points = [Point(2) for _ in range(n)]
    
    for gate in gates:
        points[gate-1].type = 0
    
    for summit in summits:
        points[summit-1].type = 1
    
    for path in paths:
        p1, p2, t = path
        points[p1-1].path.append([p2, t])
        points[p2-1].path.append([p1, t])
    
    intensities = dijkstra(points=points, gates=gates)
    candidate = [[intensities[points[summit-1]], summit] for summit in summits]
    answer = min(candidate)[::-1]
    return answer


t1 = {
    'n': 7,
    'paths': [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    'gates': [2],
    'summits': [3, 4],
}

solution(**t1)