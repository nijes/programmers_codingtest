def solution(numbers):

    answer = []

    for num in numbers:
        if num%2 == 0:
            answer.append(num + 1)
        else:
            bin_num = bin(num)
            if '01' in bin_num:
                bin_num = bin_num[::-1].replace('10', '01', 1)[::-1]
            else:
                bin_num = bin_num.replace('0b1', '10', 1)
            answer.append(int(bin_num, 2))

    return answer