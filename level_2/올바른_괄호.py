def solution(s):
    count = 0
    for i in range(len(s)):
        count += 1 if s[i] == '(' else -1
        if count < 0:
            return False
    return True if count == 0 else False