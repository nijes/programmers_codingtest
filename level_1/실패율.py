def solution(N, stages):
    failrate = {}
    for stage in range(1, N+1):
        total, fail = 0, 0
        for user in stages:
            if user >= stage:
                total += 1
            if user == stage:
                fail += 1
        failrate[stage] = 0 if total == 0 else fail/total
    return [k for k, v in sorted(failrate.items(), key=lambda x:-x[1])]