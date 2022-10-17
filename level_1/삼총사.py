from itertools import combinations

def solution_1(number):
    return sum([1 for i in combinations(number, 3) if sum(i) == 0])


def solution_2(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer