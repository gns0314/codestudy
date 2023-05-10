def solution(slice, n):
    answer = 0
    if slice >= n:
        answer = 1
    else:
        answer = ((n-1) // slice) + 1
    return answer