def solution(arr):
    answer = []
    a = []
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
            answer = arr[a[0]:a[-1]+1]
        elif a == []:
            answer = [-1]
    return answer