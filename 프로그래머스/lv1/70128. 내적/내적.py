
def solution(a, b):
    data = list(zip(a,b))
    answer = 0
    for i,j in data:
        answer += i*j
    return answer

