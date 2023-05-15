def solution(balls, share):
    return fac(balls)/(fac(balls - share) * fac(share))

def fac(a):
    b = 1
    for i in range(1, a + 1):
        b *= i
    return b