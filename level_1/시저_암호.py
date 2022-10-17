def solution(s, n):
    s = list(s)
    l_str = 'abcdefghijklmnopqrstuvwxyz'
    u_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for idx in range(len(s)):
        if s[idx] == ' ':
            s[idx] = s[idx]
        elif s[idx].islower():
            s[idx] = l_str[(l_str.index(s[idx]) + n) % 26]
        elif s[idx].isupper():
            s[idx] = u_str[(u_str.index(s[idx]) + n) % 26]
    return ''.join(s)

#참고 : ord()