def solution(s):
    return ''.join([s[i].upper() if i==0 or s[i-1]==' ' else s[i].lower() for i in range(len(s))])