def solution(want, number, discount):
    imp = set()
    for i in range(len(want)):
        for j in range(len(discount)):
            if discount[j:j+10].count(want[i]) < number[i]:
                imp.add(j)
    return len(discount)-len(imp)