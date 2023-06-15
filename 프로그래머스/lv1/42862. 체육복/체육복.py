def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    con = lost & reserve

    reserve -= con
    lost -= con

    answer = n - len(lost)
    if n == answer:
        return n

    rev = []

    for i in reserve:
        if i - 1 in lost and i not in rev:
            lost -= {i-1}
            rev.append(i)
            answer += 1
        elif i + 1 in lost and i not in rev:
            lost -= {i+1}
            rev.append(i)
            answer += 1

    return answer