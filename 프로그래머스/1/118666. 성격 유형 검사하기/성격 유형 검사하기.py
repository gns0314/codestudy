def solution(survey, choices):
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    test = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    tmp = []
    answer = ''
    for i in range(len(survey)):
        if choices[i] > 4:
            tmp += [survey[i][1],score[choices[i]]]
        elif choices[i] < 4:
            tmp += [survey[i][0],score[choices[i]]]
    for i in range(len(tmp)-1):
        if i % 2 == 0:
            test[tmp[i]] += tmp[i+1]
    for i in range(0, len(test), 2):
        first_key, second_key = list(test.keys())[i], list(test.keys())[i + 1]
        first_value, second_value = test[first_key], test[second_key]

        if first_value > second_value:
            answer += first_key
        elif first_value < second_value:
            answer += second_key
        else:
            answer += first_key
        
    return answer