def solution(hp):
    answer = 0
    a = 0
    b = 0
    a += hp // 5
    b += (hp - a * 5) // 3
    answer = a + b + (hp - (a * 5) - (b * 3))
    return answer