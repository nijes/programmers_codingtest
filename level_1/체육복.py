def solution(n, lost, reserve):
    for i in range(len(lost)-1, -1, -1):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
    lost.sort()
    reserve.sort()
    for st in lost:
        if st-1 in reserve:
            reserve.remove(st-1)
        elif st+1 in reserve:
            reserve.remove(st+1)
        else:
            n -= 1
    return n