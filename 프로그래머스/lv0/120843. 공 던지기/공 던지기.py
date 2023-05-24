def solution(numbers, k):
    if len(numbers) % 2 == 0:
        answer = []
        for i in range(0,len(numbers),2):
            answer.append(numbers[i])
        return answer[(k % len(answer)) - 1]
    else:
        answer = []
        for j in range(2):
            for s in range(j,len(numbers),2):
                answer.append(numbers[s])
        return answer[(k % len(answer)) - 1]
    return answer