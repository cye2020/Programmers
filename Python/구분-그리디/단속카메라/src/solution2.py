def solution2(routes):
    answer = 0
    capture = 0
    sorted_in = sorted(routes, key=lambda x: x[0])
    sorted_out = sorted(routes, key=lambda x: x[1])
    while capture < len(routes):
        max_in = sorted_in.pop()[0]
        for i in range(len(sorted_out)-1, -1, -1):
            route = sorted_out[i]
            if route[1] >= max_in:
                capture += 1
                sorted_out.pop()
            else:
                break
        answer += 1
        sorted_in = sorted(sorted_out, key=lambda x: x[0])
    
    return answer