def solution(n, m):
    gcd, lcm = min(n, m), max(n, m)
    for i in range(min(n, m), 0, -1):
        if n%i == 0 and m%i == 0:
            gcd = i
            break
    for j in range(max(n,m), n*m+1):
        if j%n == 0 and j%m == 0:
            lcm = j
            break
    return [gcd, lcm]