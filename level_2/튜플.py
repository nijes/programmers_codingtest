def solution(s):
    lst = s[2:len(s)-2].split('},{')
    lst.sort(key = lambda x : len(x))
    for i in range(len(lst)):
        temp = [int(x) for x in lst[i].split(',')]
        for j in range(i):
            temp.remove(lst[j])
        lst[i] = temp[0]
    return lst