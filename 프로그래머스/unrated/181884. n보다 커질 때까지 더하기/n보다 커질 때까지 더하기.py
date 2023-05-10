def solution(numbers, n):
    answer = 0
    b = 0
    for i in numbers:
        b += i
        if b > n:
            answer = b
            break
    return answer