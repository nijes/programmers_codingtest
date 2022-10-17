def solution(n, arr1, arr2):
    arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    arr2 = [bin(x)[2:].zfill(n) for x in arr2]
    return [''.join(' ' if arr1[i][j]=='0' and arr2[i][j] =='0' else '#' for j in range(n)) for i in range(n)]