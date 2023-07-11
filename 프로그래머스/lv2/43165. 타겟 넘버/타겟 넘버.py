def solution(numbers, target):
    def calc(i, sum):
        nonlocal answer
        if i == len(numbers):
            if sum == target:
                answer += 1
            return
        calc(i+1, sum + numbers[i])
        calc(i+1, sum - numbers[i])
    answer = 0
    calc(0, 0)
    return answer