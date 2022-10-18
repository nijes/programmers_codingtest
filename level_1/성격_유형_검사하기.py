def solution(survey, choices):
    answer = ''
    type_dic = {'R': 0, 'C': 0, 'J': 0, 'A': 0}
    score = list(map(lambda x: 4 - x, choices))
    for i in range(len(survey)):
        if survey[i][0] == 'R':
            type_dic['R'] += score[i]
        elif survey[i][0] == 'T':
            type_dic['R'] -= score[i]
        elif survey[i][0] == 'C':
            type_dic['C'] += score[i]
        elif survey[i][0] == 'F':
            type_dic['C'] -= score[i]
        elif survey[i][0] == 'J':
            type_dic['J'] += score[i]
        elif survey[i][0] == 'M':
            type_dic['J'] -= score[i]
        elif survey[i][0] == 'A':
            type_dic['A'] += score[i]
        else:
            type_dic['A'] -= score[i]

    answer += 'R' if type_dic['R'] >= 0 else 'T'
    answer += 'C' if type_dic['C'] >= 0 else 'F'
    answer += 'J' if type_dic['J'] >= 0 else 'M'
    answer += 'A' if type_dic['A'] >= 0 else 'N'

    return (answer)