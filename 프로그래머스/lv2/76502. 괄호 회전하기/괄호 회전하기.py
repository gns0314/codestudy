def solution(s):
    answer = 0
    for i in range(len(s)):
        tmp = s[i:]+s[:i]
        while True:
            length=len(tmp)
            tmp=tmp.replace("()","")
            tmp=tmp.replace("{}","")
            tmp=tmp.replace("[]","")
            if len(tmp) == 0:
                answer += 1
                break
            if length == len(tmp):
                break
    return answer