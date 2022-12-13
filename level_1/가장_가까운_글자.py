def solution(s):
    answer = []
    for i in range(len(s)):
        char = s[i]
        j = s.find(char)
        if i == j:
            answer.append(-1)
        else:
            answer.append(i-j)
            s = s.replace(char, ' ', 1)
    return answer