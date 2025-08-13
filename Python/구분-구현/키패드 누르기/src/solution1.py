def solution(numbers, hand):
    answer = ''
    left = {1: 3, 4: 2, 7: 1}
    right = {3: 3, 6: 2, 9: 1}
    middle = {2: 3, 5: 2, 8: 1, 0: 0}
    
    lhand = [1, 0]
    rhand = [1, 0]
    
    for n in numbers:
        if n in left.keys():
            answer += 'L'
            lhand = [1, left[n]]
        elif n in right.keys():
            answer += 'R'
            rhand = [1, right[n]]
        else:
            ldist = abs(lhand[1] - middle[n]) + lhand[0]
            rdist = abs(rhand[1] - middle[n]) + rhand[0]
            if ldist < rdist:
                answer += 'L'
                lhand = [0, middle[n]]
            elif ldist > rdist:
                answer += 'R'
                rhand = [0, middle[n]]
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = [0, middle[n]]
                else:
                    answer += 'R'
                    rhand = [0, middle[n]]
    return answer