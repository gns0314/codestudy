def solution(numer1, denom1, numer2, denom2):
    lcm = denom1 * denom2
    # 두 분수의 분자를 공통 분모로 변환
    numer1 *= denom2
    numer2 *= denom1
    # 분자의 합을 구함
    numer = numer1 + numer2
    # 합의 분자와 분모의 최대공약수를 구함
    gcd = find_gcd(numer, lcm)
    # 기약 분수로 만듦
    numer //= gcd
    lcm //= gcd
    return [numer, lcm]

# 최대공약수를 구하는 함수
def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a