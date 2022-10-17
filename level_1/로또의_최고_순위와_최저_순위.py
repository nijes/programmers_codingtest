def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = 0
    for num in lottos:
        if num in win_nums:
            match_count += 1
    return list(map(lambda x : x if x < 7 else 6, [7-(zero_count+match_count), 7-(match_count)]))