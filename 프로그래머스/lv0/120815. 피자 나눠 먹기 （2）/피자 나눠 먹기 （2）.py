def solution(n):
    answer = 0
    if n % 6 == 0:
        answer = n//6
    else:
        answer = (n*6 / gcd(n,6)) // 6
    return answer

def gcd(a,b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a