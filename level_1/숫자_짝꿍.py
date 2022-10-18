def solution(X, Y):
    answer = ''
    x_lst = [0] * 10
    y_lst = [0] * 10
    for i in range(len(X)):
        x_lst[int(X[i])] += 1
    for i in range(len(Y)):
        y_lst[int(Y[i])] += 1

    ans_lst = list(map(lambda x, y: min(x, y), x_lst, y_lst))

    for idx in range(9, -1, -1):
        answer += str(idx) * ans_lst[idx]

    return '-1' if len(answer) == 0 else '0' if answer[0] == '0' else answer