def solution(people, limit):
    people.sort(reverse=True)
    i, j = 0, -1
    while i-j <= len(people):
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            i += 1
    return i