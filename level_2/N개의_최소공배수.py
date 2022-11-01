def solution(arr):
    for i in range(1, len(arr)):
        arr[0] = lcm(arr[0], arr[i])
    return arr[0]

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
def lcm(a, b):
    return a * b / gcd(a, b)