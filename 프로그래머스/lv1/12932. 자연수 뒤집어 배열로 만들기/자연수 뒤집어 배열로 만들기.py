def solution(n):
    answer = []
    n = str(n)[::-1]
    for i in range(len(str(n))):
        answer.append(int(n[i]))
    return answer