def solution(id_list, report, k):
    reported_num = {id: 0 for id in id_list}

    report = list(set(report))
    for elem in report:
        reported_num[elem.split(' ')[1]] += 1

    stop_id = [key for key, val in reported_num.items() if val >= k]

    reported_num = {id: 0 for id in id_list}
    for elem in report:
        if elem.split(' ')[1] in stop_id:
            reported_num[elem.split(' ')[0]] += 1

    return [val for key, val in reported_num.items()]