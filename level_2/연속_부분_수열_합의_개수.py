def solution(elements):
    answer = set()
    num = len(elements)
    elements = elements*2
    for start in range(num):
        for leng in range(1, num+1):
            answer.add(sum(elements[start:start+leng]))
    return len(answer)