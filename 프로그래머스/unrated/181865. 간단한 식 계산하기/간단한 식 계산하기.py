def solution(binomial):
    answer = 0
    i = binomial.split(' ')
    if i[1] == '*':
        answer = int(i[0]) * int(i[2])
    elif i[1] == '+':
        answer = int(i[0]) + int(i[2])
    elif i[1] == '-':
        answer = int(i[0]) - int(i[2])
    elif i[1] == '/':
        answer = int(i[0]) / int(i[2])
    return answer