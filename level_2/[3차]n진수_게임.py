def solution(n, t, m, p):
    all_num = '0'
    num = 1
    while len(all_num) < m*t:
        all_num += to_jinsu(num, n)
        num += 1
    return ''.join(all_num[p+i*m-1] for i in range(t))

def to_jinsu(num, n):
    jinsu = ''
    num_dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
               8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while num > 0:
        jinsu += num_dic[num%n]
        num = num//n
    return jinsu[::-1]