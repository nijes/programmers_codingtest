def solution(priorities, location):
    priorities = [[i, p] for i, p in enumerate(priorities)]

    prints = []
    while priorities:
        if priorities[0][1] == max(map(lambda x: x[1], priorities)):
            prints.append(priorities[0][0])
        else:
            priorities.append(priorities[0])
        del priorities[0]

    return prints.index(location) + 1