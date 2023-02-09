import copy

maxDiff = 0
result = []


def solution(n, info):
    answer = []
    candi = [0] * 11
    k = n
    peachScore = 0
    for idx, value in enumerate(info):
        candi[idx] = value + 1
        if value >= 1:
            peachScore += (10 - idx)

    def dfs(old_candi, idx, leave, new_candi, peachScore, lionScore):
        global maxDiff
        global result

        if leave < 0:
            return

        if idx >= len(old_candi):
            if leave == 0:
                if peachScore < lionScore and maxDiff < lionScore - peachScore:
                    maxDiff = lionScore - peachScore
                    temp = copy.deepcopy(new_candi)
                    result = temp
                elif peachScore < lionScore and maxDiff == lionScore - peachScore:
                    for i in range(10, -1, -1):
                        if result[i] < new_candi[i]:
                            temp = copy.deepcopy(new_candi)
                            result = temp
                            break
                        elif result[i] == new_candi[i]:
                            continue
                        else:
                            break
            else:
                new_candi[10] += leave
                dfs(old_candi, idx, 0, new_candi, peachScore, lionScore)
                new_candi[10] -= leave
            return

        if leave == 0:
            if peachScore < lionScore and maxDiff < lionScore - peachScore:
                maxDiff = lionScore - peachScore
                temp = copy.deepcopy(new_candi)
                result = temp
            elif peachScore < lionScore and maxDiff == lionScore - peachScore:
                for i in range(10, -1, -1):
                    if result[i] < new_candi[i]:
                        temp = copy.deepcopy(new_candi)
                        result = temp
                        break
                    elif result[i] == new_candi[i]:
                        continue
                    else:
                        break
            return

        # 무시 하고 넘어가기
        dfs(old_candi, idx + 1, leave, new_candi, peachScore, lionScore)

        # 무시하지 않고 화살 쏘기
        if old_candi[idx] >= 2:
            new_candi[idx] += old_candi[idx]
            dfs(old_candi, idx + 1, leave - old_candi[idx], new_candi, peachScore - (10 - idx), lionScore + (10 - idx))
            new_candi[idx] -= old_candi[idx]
        else:
            new_candi[idx] += old_candi[idx]
            dfs(old_candi, idx + 1, leave - 1, new_candi, peachScore, lionScore + (10 - idx))
            new_candi[idx] -= old_candi[idx]


    dfs(candi, 0, k, [0] * 11, peachScore, 0)

    if maxDiff == 0:
        return [-1]
    return result


# 남의 코드 (chty94)