def solution(array):
    answer = -1
    a = list(set(array))
    b = [array.count(i) for i in a]
    
    if b.count(max(b)) == 1:
        answer = a[b.index(max(b))]
    return answer
