def solution(s):
    count, zero_num = 0, 0
    while s != '1':
        count += 1
        zero_num += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
    return [count, zero_num]