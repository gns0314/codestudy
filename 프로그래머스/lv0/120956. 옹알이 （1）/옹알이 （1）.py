def solution(babbling):
    answer = 0
    b = ''
    dic = ["aya", "ye", "woo", "ma"]
    for i in babbling :
        b = i
        for j in dic :
            b = b.replace(j, '_',1)
            if len(b.replace('_','')) == 0 :
                answer += 1
                break
    return answer