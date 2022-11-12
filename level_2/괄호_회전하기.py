def solution(s):
    answer = 0
    for i in range(len(s)):
        s1 = s[i:] + s[:i]
        while s1:
            if '()' not in s1 and '{}' not in s1 and '[]' not in s1:
                break
            for br in ['()', '{}', '[]']:
                while br in s1:
                    s1 = s1.replace(br, '')
        if not s1:
            answer += 1
    return answer