def solution(my_string, m, c):
    answer = ''
    temp = []
    for i in range(len(my_string)//m):
        a = i * m
        b = (i+1)*m 
        temp.append(my_string[a:b])
        answer += temp[i][c-1]
    return answer
