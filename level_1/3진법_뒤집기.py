def solution(n):
    n3 = ''
    while n > 0:
        n3 += str(n%3)
        n = n//3
    return int(n3, 3)