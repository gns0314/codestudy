def solution(food):
    answer = ''
    a = ''
    for i in range(1, len(food)):
        if food[i] % 2 == 0 :
            a += str(i) * (food[i] //2)
        else:
            a += str(i) * ((food[i] - 1) //2)
    answer = a + '0' + a[::-1]
    return answer