def solution(today, terms, privacies):
    answer = []

    t_year, t_month, t_day = map(lambda x: int(x), today.split('.'))
    today = t_year * 12 * 28 + t_month * 28 + t_day

    term_dic = dict()
    for term in terms:
        term_dic[term[0]] = int(term.split(' ')[1])

    for i in range(len(privacies)):
        term = term_dic[privacies[i][-1]]
        year, month, day = map(lambda x: int(x), privacies[i].split(" ")[0].split('.'))
        year += (month + term - 1) // 12
        month = (month + term - 1) % 12 + 1
        if year * 12 * 28 + month * 28 + day <= today:
            answer.append(i + 1)

    return answer