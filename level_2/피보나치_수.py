def solution(n):
    fibo_arr = [0, 1]
    for i in range(2, n+1):
        fibo_arr.append((fibo_arr[i-1] + fibo_arr[i-2])%1234567)
    return fibo_arr[n]