def solution(n):
    answer = 0
    count = n + 1
    while bin(count).count('1') != bin(n).count('1'):
        count += 1
    return count