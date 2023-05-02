def solution(arr, queries):
    answer = arr
    for q in queries:
        i , j = q[0], q[1]
        arr[i], arr[j] = arr[j], arr[i]
        
    return answer