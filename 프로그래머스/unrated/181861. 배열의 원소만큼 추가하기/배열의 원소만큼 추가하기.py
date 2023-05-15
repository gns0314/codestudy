def solution(arr):
    answer = []
    for i in arr:
        for j in [i] * i:
            answer.append(j)
    return answer
