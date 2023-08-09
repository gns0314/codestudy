def solution(s):
    count = 0
    zero_count = 0
    while s != '1':
        count += 1
        num = len(s)
        s = s.count("1")*"1"
        zero_count += num - len(s)
        s = len(s)
        s = bin(s)[2:]
    answer = [count,zero_count]
    return answer