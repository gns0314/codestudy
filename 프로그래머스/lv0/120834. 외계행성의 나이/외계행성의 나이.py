def solution(age):
    answer = ''
    b = dict(enumerate('abcdefghijklmnopqrstuvwxyz',0))
    for i in str(age):
        answer += b[int(i)]
    return answer