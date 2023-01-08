def solution(dirs):
    link = set()
    b_loc = [0, 0]
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            loc = [b_loc[0], b_loc[1] + 1]
        elif dirs[i] == 'D':
            loc = [b_loc[0], b_loc[1] - 1]
        elif dirs[i] == 'R':
            loc = [b_loc[0] + 1, b_loc[1]]
        else:
            loc = [b_loc[0] - 1, b_loc[1]]

        if abs(loc[0]) <= 5 and abs(loc[1]) <= 5:
            link.add((b_loc[0] + loc[0], b_loc[1] + loc[1]))
            b_loc = loc

    return len(link)