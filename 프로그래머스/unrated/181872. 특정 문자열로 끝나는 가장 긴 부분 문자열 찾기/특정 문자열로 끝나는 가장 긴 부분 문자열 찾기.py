def solution(myString, pat):
    n = len(myString)
    m = len(pat)
    for i in range(n - 1, -1, -1): 
        if myString[i] == pat[m - 1]:
            if myString[i-m+1:i+1] == pat:
                return myString[:i+1]
    return ""