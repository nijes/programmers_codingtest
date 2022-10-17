def solution(arr):
    answer = [arr[0]]
    for elem in arr:
        if answer[len(answer)-1] != elem:
            answer.append(elem)
    return answer