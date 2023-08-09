def solution(s):
    answer = -1
    tmp = []
    for i in s:
        tmp += i
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()
    if len(tmp) == 0:
        return 1
    else:
        return 0