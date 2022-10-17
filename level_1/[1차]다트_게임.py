def solution(dartResult):
    answer, idx, b_score = 0, 0, 0
    while idx < len(dartResult):
        score = 10 if dartResult[idx + 1].isdecimal() else int(dartResult[idx])
        idx += 2 if dartResult[idx + 1].isdecimal() else 1

        bonus = (lambda x: 3 if x == 'T' else 2 if x == 'D' else 1)(dartResult[idx])
        idx += 1

        if idx == len(dartResult) or dartResult[idx].isdecimal():
            answer += score ** bonus
            b_score = score ** bonus
        elif dartResult[idx] == '#':
            answer += -score ** bonus
            b_score = -score ** bonus
            idx += 1
        else:
            answer += b_score + 2 * score ** bonus
            b_score = 2 * score ** bonus
            idx += 1

    return answer