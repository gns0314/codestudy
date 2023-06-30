def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)
            else:
                return False
        else:
            if i == ')':
                stack.pop()
            else:
                stack.append(i)
    return True if len(stack) == 0 else False