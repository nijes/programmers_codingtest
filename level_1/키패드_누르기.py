def solution(numbers, hand):
    answer = ''
    fin_dic = {1:[1,1], 2:[1,2], 3:[1,3], 4:[2,1], 5:[2,2], 6:[2,3], 7:[3,1], 8:[3,2], 9:[3,3], 0:[4,2]}
    left = [4,1]
    right = [4,3]
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = fin_dic[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            right = fin_dic[num]
        else:
            left_dis = abs(fin_dic[num][0] - left[0]) + abs(fin_dic[num][1] - left[1])
            right_dis = abs(fin_dic[num][0] - right[0]) + abs(fin_dic[num][1] - right[1])
            if (left_dis == right_dis and hand =='left') or left_dis < right_dis:
                answer += 'L'
                left = fin_dic[num]
            else:
                answer += 'R'
                right = fin_dic[num]
    return answer