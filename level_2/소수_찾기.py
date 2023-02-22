from itertools import permutations

def solution(numbers):
    prime_list, not_prime_list = [], []
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            chk_int = int(''.join(j))
            if chk_int in prime_list or chk_int in not_prime_list:
                pass
            else:
                if prime_chk(chk_int) == 1:
                    prime_list.append(chk_int)
                else:
                    not_prime_list.append(chk_int)
    return len(prime_list)


def prime_chk(number):
    if number in [0, 1]:
        return 0
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: return 0
    else:
        return 1