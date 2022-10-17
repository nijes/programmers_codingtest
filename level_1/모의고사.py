def solution(answers):
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cor_dic = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if answers[i] == ans_1[i%5]:
            cor_dic[1] += 1
        if answers[i] == ans_2[i%8]:
            cor_dic[2] += 1
        if answers[i] == ans_3[i%10]:
            cor_dic[3] += 1
    return [k for k, v in cor_dic.items() if v == max(cor_dic.values())]