def solution(n, words):
    answer = []
    tmp = []
    for j in range(len(words)):
        if words[j] in tmp:
            answer.append(((j+1)%n if (j+1)%n !=0 else n))
            answer.append((j//n)+1 if j//n  != 0 else 1)
            return answer
        if len(tmp) != 0:
            if tmp[-1][-1] != words[j][0]:
                answer.append(((j+1)%n if (j+1)%n !=0 else n))
                answer.append((j//n)+1 if j//n  != 0 else 1)
                return answer
        tmp.append(words[j])
            
    if len(set(words)) == len(tmp):
        return [0,0]
        