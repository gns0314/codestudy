def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        row = i // n
        col = i % n
        max_val = max(row + 1, col + 1)
        answer.append(max_val)

    return answer
