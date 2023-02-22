def solution(cards1, cards2, goal):

    card1 = cards1.pop(0)
    card2 = cards2.pop(0)

    while goal:
        word = goal.pop(0)
        if word == card1:
            card1 = cards1.pop(0) if cards1 else ''
        elif word == card2:
            card2 = cards2.pop(0) if cards2 else ''
        else:
            return 'No'

    return 'Yes'