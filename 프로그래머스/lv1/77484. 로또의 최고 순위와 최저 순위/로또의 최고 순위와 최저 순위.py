def solution(lottos, win_nums):
    answer = [0,0]
    min_count = 0
    max_count = 0
    for i in lottos:
        if i in win_nums:
            min_count += 1
        elif i == 0:
            max_count += 1
    max_count += min_count
    if min_count == 6:
        answer[1] = 1
    elif min_count == 5:
        answer[1] = 2
    elif min_count == 4:
        answer[1] = 3
    elif min_count == 3:
        answer[1] = 4
    elif min_count == 2:
        answer[1] = 5
    else:
        answer[1] = 6
        
    if max_count == 6:
        answer[0] = 1
    elif max_count == 5:
        answer[0] = 2
    elif max_count == 4:
        answer[0] = 3
    elif max_count == 3:
        answer[0] = 4
    elif max_count == 2:
        answer[0] = 5
    else:
        answer[0] = 6
    return answer