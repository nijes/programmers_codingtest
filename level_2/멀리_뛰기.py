from math import comb
def solution(n):
    return sum([comb(n-i,i)%1234567 for i in range(n//2+1)])%1234567