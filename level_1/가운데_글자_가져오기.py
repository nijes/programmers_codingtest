def solution(s):
    return s[len(s)//2] if len(s)%2 == 1 else s[(len(s)-1)//2:(len(s)+1)//2+1]