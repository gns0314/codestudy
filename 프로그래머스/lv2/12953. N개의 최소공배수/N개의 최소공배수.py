def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
def solution(arr):
    answer = 0
    b = arr[0]
    for i in range(1,len(arr)):
        b = lcm(b,arr[i])
    return b

