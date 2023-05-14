def solution(myString):
    answer = []
    for i in myString.split('x'):
        if i == '':
            answer.append(0)
        else:
            answer.append(len(i))
    return answer