def solution(myString):
    answer = []
    for i in sorted(myString.strip('x').split('x')):
        if i != '':
            answer.append(i)
    return answer