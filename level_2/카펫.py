def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0 and (i+2) * (yellow//i+2) == brown+yellow:
            return [yellow//i+2, i+2]