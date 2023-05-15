def solution(arr, k):
    answer = []
    num_set = set()
    
    for num in arr:
        if num not in num_set:
            num_set.add(num)
            answer.append(num)
        
        if len(answer) == k:
            break
    
    while len(answer) < k:
        answer.append(-1)
    
    return answer