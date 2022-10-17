def solution(arr1, arr2):
    answer = []
    for r in range(len(arr1)):
        answer.append([])
        for c in range(len(arr1[0])):
            answer[r].append(arr1[r][c] + arr2[r][c])
    return answer