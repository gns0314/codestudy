from collections import deque

def solution(queue1, queue2):
    count = 0
    total_sum = sum(queue1) + sum(queue2)
    target = total_sum / 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    limit = len(q1) + len(q2)
    
    if sum_q1+sum_q2 % 2 == 1:
        return -1
    
    while sum_q1 != target:
        if count > limit*2:
            return -1
        if target < sum_q1:
            extracted = q1.popleft()
            if extracted > target:
                return -1
            q2.append(extracted)
            count += 1
            sum_q1 -= extracted
            sum_q2 += extracted
        else:
            extracted = q2.popleft()
            if extracted > target:
                return -1
            q1.append(extracted)
            count += 1
            sum_q1 += extracted
            sum_q2 -= extracted
    
    return count
