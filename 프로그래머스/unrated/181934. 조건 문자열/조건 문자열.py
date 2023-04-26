def solution(ineq, eq, n, m):
    answer = ''
    if eq == "=" and ineq == ">" and n >= m:
        answer = 1
    elif eq == "=" and ineq == "<" and n <= m:
        answer = 1
    elif eq == "!" and ineq == ">" and n > m:
        answer = 1
    elif eq == "!" and ineq == "<" and n < m:
        answer = 1 
    else:
        answer = 0
    return answer
