def solution(n, k):
    answer = 0

    n_k = ''
    while n > 0:
        n_k = str(n % k) + n_k
        n = n // k

    lst = n_k.split('0')

    for i in lst:
        if i == '' or i == '1':
            pass
        elif i == '2':
            answer += 1
        else:
            i = int(i)
            for j in range(2, int(i ** 0.5) + 1):
                if int(i) % j == 0:
                    break
            else:
                answer += 1

    return answer