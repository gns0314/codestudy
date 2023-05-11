def solution(money):
    answer = []
    a = []
    while money >= 5500:
        money = money - 5500
        a.append(money)
    answer = [len(a), money]
    return answer