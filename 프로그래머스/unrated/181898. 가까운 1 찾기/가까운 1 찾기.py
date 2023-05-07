def solution(arr, idx):
    answer = 0
    for i in range(len(arr)):
        if (i >= idx) and arr[i] == 1:
            answer = i
            break
        else:
            answer = -1
    return answer