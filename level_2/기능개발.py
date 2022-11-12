from math import ceil
def solution(progresses, speeds):
    days = [ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    answer = [1]
    d = 0
    for i in range(1, len(days)):
        if days[i] <= days[d]:
            answer[-1] += 1
        else:
            answer.append(1)
            d = i
    return answer