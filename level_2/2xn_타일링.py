def solution(n):
    answer = 1
    tmp1, tmp2 = 1, 0
    for i in range(n):
        answer += tmp2
        tmp2 = tmp1
        tmp1 = answer
    return answer%1000000007