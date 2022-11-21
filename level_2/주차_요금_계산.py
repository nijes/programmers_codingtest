from math import ceil


def solution(fees, records):
    records.sort(key=(lambda x: x[6:10]))
    rec_dic = {}
    for record in records:
        car_num = record[6:10]
        if car_num in rec_dic.keys():
            if record[-1] == 'T':
                rec_dic[car_num] -= 23 * 60 + 59 - int(record[:2]) * 60 - int(record[3:5])
            else:
                rec_dic[car_num] += 23 * 60 + 59 - int(record[:2]) * 60 - int(record[3:5])
        else:
            rec_dic[car_num] = 23 * 60 + 59 - int(record[:2]) * 60 - int(record[3:5])

    answer = []
    for time in rec_dic.values():
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3]
            answer.append(fee)

    return answer