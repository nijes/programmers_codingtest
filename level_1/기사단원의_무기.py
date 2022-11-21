def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        answer += power if yaksu(i)>limit else yaksu(i)
    return answer

def yaksu(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            count += 2
    return count - 1 if int(n**0.5)==n**0.5 else count