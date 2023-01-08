from collections import Counter

def solution(k, tangerine):
    tangerine = Counter(tangerine).most_common()
    answer = 0
    while k > 0:
        k -= tangerine.pop(0)[1]
        answer += 1
    return answer