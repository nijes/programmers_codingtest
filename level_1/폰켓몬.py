def solution_1(nums):
    max = len(nums)//2
    kind = len(list(set(nums)))
    return max if kind >= max else kind

def solution_2(nums):
    answer = 0
    for _ in range(len(nums)//2):
        if len(nums) == 0:
            break
        poke = nums[0]
        answer += 1
        while poke in nums:
            nums.remove(poke)
    return answer