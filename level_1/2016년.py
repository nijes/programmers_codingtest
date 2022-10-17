def solution(a, b):
    day_dic = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    day = 30*(a-1) + b + (lambda a : (a+1)//2-1 if a>8 else a//2-1 if a>2 else 1 if a>1 else 0)(a)
    return day_dic[day % 7]