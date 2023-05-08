def solution(arr, intervals):
    answer = []
    for i,e in intervals:
        answer += arr[i:e+1]
    return answer