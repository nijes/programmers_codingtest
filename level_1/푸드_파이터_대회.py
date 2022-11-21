def solution(food):
    half_food = ''
    for i in range(1,len(food)):
        half_food += str(i)*(food[i]//2)
    return half_food + '0' + half_food[::-1]