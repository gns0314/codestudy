def solution(n):
    # 초기 피보나치 수
    fib = [0, 1]
    
    # n이 2보다 작거나 같은 경우, 바로 값을 반환
    if n <= 1:
        return fib[n]
    
    # n번째 피보나치 수 계산
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1234567)
    
    return fib[n]