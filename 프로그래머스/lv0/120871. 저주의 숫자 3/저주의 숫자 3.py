def solution(n):
    return [i for i in range(1, 1001) if i % 3 != 0 and not('3' in str(i))][n-1]