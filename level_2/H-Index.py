def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations), -1, -1):
        if citations[i-1] >= i:
            return i