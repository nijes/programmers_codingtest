def solution(str1, str2):
    lst1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    lst2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    inter = []
    lst2_temp = lst2.copy()
    for e in lst1:
        if e in lst2_temp:
            inter.append(e)
            lst2_temp.remove(e)

    union = lst1.copy()
    lst1_temp = lst1.copy()
    for e in lst2:
        if e in lst1_temp:
            lst1_temp.remove(e)
        else:
            union.append(e)

    return int(len(inter)/len(union)*65536) if union else 65536