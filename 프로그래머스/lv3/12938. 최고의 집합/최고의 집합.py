def solution(n, s):
    if n > s:
        return [-1] 

    i = s // n 
    j = s % n   

    result = [i] * (n - j) + [i + 1] * j

    return result