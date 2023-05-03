def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i == 0:
            continue
        if set(str(i)) <= {'0', '5'}:
            answer.append(i)
    if not answer:
        answer.append(-1)
            
    return answer