def solution(number):
    answer = 0
    a = 0
    for i in number:
        a += int(i)
        answer = a % 9
    return answer