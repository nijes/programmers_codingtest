def solution_1(x):
    x_div = x
    divider = 0
    for _ in range(len(str(x))):
        divider += x_div % 10
        x_div = x_div // 10
    return x % divider == 0

def solution_2(x):
    return x % sum([int(i) for i in list(str(x))]) == 0