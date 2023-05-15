def solution(arr):
    answer = []
    a = []
    for i in range(len(arr)):
        if len(answer) == 0 or arr[i] != answer[-1]:
            answer.append(arr[i])
        elif arr[i] == answer[-1]:
            answer.pop()
    if len(answer) == 0 :
        answer = [-1]
    return answer