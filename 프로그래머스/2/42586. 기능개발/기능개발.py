import math

def solution(progresses, speeds):
    answer = []
    tmp = [(100 - i) for i in progresses]
    time = [math.ceil(tmp[j] / speeds[j]) for j in range(len(speeds))]
    
    while len(time) > 0:
        temp = time.pop(0)
        count = 1

        while len(time) > 0 and time[0] <= temp:
            count += 1
            time.pop(0)

        answer.append(count)

    return answer