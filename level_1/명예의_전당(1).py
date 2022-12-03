from heapq import heappop, heappush, heapify
def solution(k, score):
    answer, honor = [], []
    heapify(honor)
    for sc in score:
        heappush(honor, sc)
        if len(honor) > k:
            heappop(honor)
        answer.append(honor[0])
    return answer