def solution(s):
    answer, i, same, diff = 0, 0, 0, 0
    for i in range(len(s)):
        if same == diff:
            check_char = s[i]
            same, diff = 1, 0
            answer += 1
        elif s[i] == check_char:
            same += 1
        else:
            diff += 1
    return answer