def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: x*3, reverse=True)

    return '0' if numbers[0]=='0' else ''.join(numbers)