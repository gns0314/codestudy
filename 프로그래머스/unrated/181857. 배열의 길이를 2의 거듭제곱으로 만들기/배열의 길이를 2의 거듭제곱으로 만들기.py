def solution(arr):
    answer = []
    while len(arr) not in list(map(lambda x:2**x, range(11))):
            arr.append(0)
    answer = arr
    return answer