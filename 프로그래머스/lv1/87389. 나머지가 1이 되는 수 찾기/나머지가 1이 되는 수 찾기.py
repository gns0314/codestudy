def solution(n):
    answer = 0
    count = 1
    while n % count != 1:
        count += 1
    return count