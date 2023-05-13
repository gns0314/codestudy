def solution(name, yearning, photo):
    c = dict(zip(name,yearning))
    answer = [sum([c[j] for j in i if j in c]) for i in photo]
    return answer