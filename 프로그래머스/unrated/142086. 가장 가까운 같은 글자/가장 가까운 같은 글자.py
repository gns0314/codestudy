def solution(s):
    answer = []
    a = []
    for i in range(len(s)):
        if s[i] not in a:
            answer.append(-1)
        elif s[i] in a:
            answer.append(i - ''.join(a).rfind(s[i]))
        a.append(s[i])   
    return answer