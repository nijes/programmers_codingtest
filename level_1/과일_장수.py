def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        box = score[i*m:(i+1)*m]
        answer += min(box) * m
    return answer