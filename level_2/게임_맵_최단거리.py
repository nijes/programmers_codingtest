from collections import deque

def solution(maps):
    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, dis = q.popleft()

        # 목적지 도달
        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            return dis

        # 이미 방문한 칸일 때
        if maps[y][x] == 0:
            continue
        # 처음 방문
        else:
            if x + 1 < len(maps[0]):
                q.append((x + 1, y, dis + 1))
            if y + 1 < len(maps):
                q.append((x, y + 1, dis + 1))
            if x - 1 >= 0:
                q.append((x - 1, y, dis + 1))
            if y - 1 >= 0:
                q.append((x, y - 1, dis + 1))
            # 방문 처리
            maps[y][x] = 0

    return -1