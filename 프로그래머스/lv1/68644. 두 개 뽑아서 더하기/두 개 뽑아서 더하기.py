import itertools
def solution(numbers):
    answer = []
    d = []
    c = itertools.combinations(numbers, 2) 
    for i in c:
        d.append(sum(i))
    d = list(set(d))
    answer = sorted(d)
    return answer