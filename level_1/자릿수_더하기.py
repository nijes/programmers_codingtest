def solution_1(n):
    answer = 0
    while n > 0:
        answer += n%10
        n = n//10
    return answer

def solution_2(n):
    return sum(map(lambda x : int(x), list(str(n))))