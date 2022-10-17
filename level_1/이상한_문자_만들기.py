def solution(s):
    answer = ''
    idx = 0
    while idx < len(s):
        if s[idx] == ' ':
            answer += ' '
            idx += 1
        else:
            start = idx
            while idx < len(s) and s[idx] != ' ':
                answer += s[idx].upper() if (idx-start)%2==0 else s[idx].lower()
                idx += 1
    return answer