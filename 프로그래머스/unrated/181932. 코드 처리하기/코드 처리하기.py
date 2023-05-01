def solution(code):
    mode = 0
    answer = ''
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx % 2 == 0:
                    answer += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != '1':
                if idx % 2 == 1:
                    answer += code[idx]
            else:
                mode = 0
    if answer == '':
        return 'EMPTY'
    else:
        return answer
    return answer