def solution(ingredient):
    count = 0
    st_search = 0
    while True:
        for i in range(st_search, len(ingredient)-3):
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                del ingredient[i:i+4]
                count += 1
                st_search = max(i-3, 0)
                break
        else:
            return count