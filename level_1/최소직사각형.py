def solution(sizes):
    # 가로,세로 중 큰 값을 앞으로
    sizes = list(map(lambda x: [x[1], x[0]] if x[0]<x[1] else [x[0], x[1]], sizes))
    w = max(sizes[i][0] for i in range(len(sizes)))
    h = max(sizes[i][1] for i in range(len(sizes)))
    return w*h