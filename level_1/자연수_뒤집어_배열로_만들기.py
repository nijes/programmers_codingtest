def solution_1(n):
    answer = []
    for _ in range(len(str(n))):
        answer.append(n%10)
        n = n//10
    return answer

def solution_2(n):
    return list(map(lambda x : int(x), list(str(n))))[::-1]