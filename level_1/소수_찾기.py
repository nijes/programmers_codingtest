def solution(n):
    p_num = 1
    for i in range(3, n+1, 2):
        p_num += 1
        for divider in range(2, int(i**0.5)+1):
            if i % divider == 0:
                p_num -= 1
                break
    return p_num