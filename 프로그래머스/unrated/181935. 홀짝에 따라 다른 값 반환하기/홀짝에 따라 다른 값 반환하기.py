def solution(n):
    answer = ''
    if n % 2 == 1:
        return sum(range(1, n+1, 2)) #sum 함수를 통해 1부터 n까지 2씩 더해가며 계산 ex)n = 7, 1부터 7까지 1+3+5+7 = 16 
                                     #n+1 이유는 n+1 전까지만 하기때문에 n까지 반복해주려면 n+1을 해줘야함
    else:
        return sum(i**2 for i in range(2, n+1, 2)) 
    return answer
