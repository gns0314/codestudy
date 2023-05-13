def solution(my_string):
    answer = []
    b = 0
    for i in range(len(my_string)):
        if my_string[i] == ' ' :
            answer.append(my_string[b:i])
            b = i + 1
    answer.append(my_string[b:])
    return answer