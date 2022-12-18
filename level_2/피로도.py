from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons):
        count, tired = 0, k
        for dungeon in order:
            if tired < dungeon[0]: break
            tired -= dungeon[1]
            count += 1
        answer = max(count, answer)
        if answer == len(dungeons): break
    return answer