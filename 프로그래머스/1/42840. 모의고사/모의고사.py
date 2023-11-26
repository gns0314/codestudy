def solution(answers):
    answer = []
    fail1 = [1,2,3,4,5]
    fail2 = [2,1,2,3,2,4,2,5]
    fail3 = [3,3,1,1,2,2,4,4,5,5]
    max_tmp = [0,0,0]
    for q in range(len(answers)):
        if len(answers) != len(fail1):
            fail1.append(fail1[q])
        if len(answers) != len(fail2):
            fail2.append(fail2[q])
        if len(answers) != len(fail3):
            fail3.append(fail3[q])
            
    for i in range(len(answers)):
        if answers[i] == fail1[i]:
            max_tmp[0] += 1
        if answers[i] == fail2[i]:
            max_tmp[1] += 1
        if answers[i] == fail3[i]:
            max_tmp[2] += 1
    
    for w in range(len(max_tmp)):
        if max_tmp[w] == max(max_tmp):
            answer.append(w+1)
    
    return answer