def solution(dot):
    answer = 0
    s, e = dot
    if s > 0 and e > 0 :
        answer = 1
    elif s < 0 and e > 0 :
        answer = 2
    elif s < 0 and e < 0 :
        answer = 3
    else:
        answer = 4
    return answer