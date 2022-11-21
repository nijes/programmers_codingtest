def solution(babbling):
    answer = 0
    for word in babbling:
        word = word.replace('aya', '1').replace('ye', '2').replace('woo', '3').replace('ma', '4')
        if word.isdecimal() and word.find('11')+word.find('22')+word.find('33')+word.find('44') == -4:
            answer += 1
    return answer