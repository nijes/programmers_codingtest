def solution(s):
    num_list = list(map(lambda x : int(x), s.split(' ')))
    return str(min(num_list)) + ' ' + str(max(num_list))