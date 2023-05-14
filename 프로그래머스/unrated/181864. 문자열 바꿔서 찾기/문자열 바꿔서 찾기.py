def solution(myString, pat):
    answer = 0
    c = ''
    for i in myString:
        if i == 'A':
            c += 'B'
        else:
            c += 'A'
        
    if pat in c:
        answer = 1
    return answer