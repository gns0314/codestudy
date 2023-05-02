def get_operation(prev, cur):
    if cur == prev + 1:
        return "w"
    elif cur == prev - 1:
        return "s"
    elif cur == prev + 10:
        return "d"
    elif cur == prev - 10:
        return "a"
def solution(numLog):
    result = ""
    for i in range(1, len(numLog)):
        prev = numLog[i-1]
        cur = numLog[i]
        op = get_operation(prev, cur)
        result += op
        prev = cur
    return result
