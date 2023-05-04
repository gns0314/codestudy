def solution(my_string):
    answer = ''
    a = set(my_string)
    for i in my_string:
        if i in a:
            answer += i
            a.remove(i)
    return answer