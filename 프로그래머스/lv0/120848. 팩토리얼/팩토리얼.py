def solution(n):
    answer = 0
    count = 1
    num = 1
    while True:
        if count * num <= n:
            count *= num
            num += 1
        else:
            break
    answer = num - 1
    return answer