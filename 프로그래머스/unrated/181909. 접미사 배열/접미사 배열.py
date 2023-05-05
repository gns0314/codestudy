def solution(my_string):
    answer = []
    a = []
    for i in range(len(my_string)):
        a.append(my_string[-(i+1):])
        answer = sorted(a)
    return answer