def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif ord(i) + n > 122 and 122 >= ord(i) >= 97:
            answer += chr(ord(i)+ n - 26)
        elif ord(i) + n > 90 and 90 >= ord(i) >= 65:
            answer += chr(ord(i)+ n - 26)
        else:
            answer += chr(ord(i)+n)
    return answer