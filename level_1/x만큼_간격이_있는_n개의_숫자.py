def solution_1(x, n):
    answer = []
    x1 = 0
    for _ in range(n):
        x1 += x
        answer.append(x1)
    return answer

def solution_2(x, n):
    if x < 0:
        return list(range(x, x*n - 1, x))
    else:
        return list(range(x, x*n + 1, x))