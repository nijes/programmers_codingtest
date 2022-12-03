import re
def solution(msg):
    answer = []
    dic = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', (i for i in range (1, 27))))
    num = 26
    while True:
        for k in sorted(dic.keys(), key=(lambda x: -len(x))):
            if re.match(k, msg):
                answer.append(dic[k])
                msg = msg[len(k):]
                if msg:
                    num += 1
                    dic[k+msg[0]] = num
                    break
                else:
                    return answer