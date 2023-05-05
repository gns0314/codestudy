def solution(my_string, n):
    answer = ''
    a = list(my_string)
    a.reverse()
    b = a[:n]
    b.reverse()
    b
    answer = ''.join(b)
    return answer