def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += i.upper()
        elif i != 'a' and i != 'A':
            answer += i.lower()
        else:
            answer += i
    return answer