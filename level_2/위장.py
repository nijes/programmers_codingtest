from functools import reduce
def solution(clothes):
    cloth_dic = {}
    for cl in clothes:
        if cl[1] in cloth_dic.keys():
            cloth_dic[cl[1]] += 1
        else:
            cloth_dic[cl[1]] = 2        
    return reduce(lambda x,y : x*y, cloth_dic.values()) - 1