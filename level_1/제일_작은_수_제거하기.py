def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min = arr[0]
        for elem in arr:
            if elem < min:
                min = elem
        arr.remove(min)
        return arr