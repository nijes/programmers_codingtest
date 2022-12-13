def solution(record):
    answer = []
    id_dic = {}

    record = list(map(lambda x: x.split(' '), record))
    for rec in record:
        if rec[0] == 'Enter':
            answer.append(f'{rec[1]}님이 들어왔습니다.')
            id_dic[rec[1]] = rec[2]
        elif rec[0] == 'Leave':
            answer.append(f'{rec[1]}님이 나갔습니다.')
        else:
            id_dic[rec[1]] = rec[2]

    for i in range(len(answer)):
        id = answer[i].split('님')[0]
        answer[i] = answer[i].replace(id, id_dic[id])

    return answer