def solution(number):
    return sum(item for item in range(number) if item%3==0 or item%5 == 0)