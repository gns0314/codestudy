def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    
    if b ** 2 > a:
        answer = 1
    else:
        answer = 0
    return answer