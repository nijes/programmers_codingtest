def solution(s, skip, index):

    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for char in skip:
        alpha.remove(char)

    return ''.join(alpha[(alpha.index(char) + index) % len(alpha)] for char in s)