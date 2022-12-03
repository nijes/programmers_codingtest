from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(len(scoville)-1):
        scoville_0 = heappop(scoville)
        if scoville_0 >= K:
            return i
        scoville_1 = heappop(scoville)
        heappush(scoville, scoville_0 + 2*scoville_1)
    return i+1 if heappop(scoville) >= K else -1