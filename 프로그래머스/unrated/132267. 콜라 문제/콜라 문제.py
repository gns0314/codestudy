def solution(a, b, n):
    answer = 0

    while(n!=0):
        d=n%a
        n=n//a
        answer+=n*b
        n = n*b + d
        if n<a:
            break  
    return answer