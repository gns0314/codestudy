def solution(emergency):
    answer = []
    a = sorted(emergency, reverse = True)
    for i in range(len(emergency)):
        answer.append(a.index(emergency[i])+1)
    return answer