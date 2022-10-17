from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        answer += 1
        num = i[0] + i[1] + i[2]
        for div in range(2, int(num**0.5)+1):
            if num % div == 0:
                answer -= 1
                break
    return answer