from itertools import permutations

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    all_combinations = set()

    # 가능한 모든 숫자 조합 생성
    for i in range(1, len(numbers) + 1):
        permutations_list = permutations(numbers, i)
        for perm in permutations_list:
            num = int("".join(perm))
            all_combinations.add(num)

    # 각 숫자 조합이 소수인지 확인
    for num in all_combinations:
        if is_prime(num):
            answer += 1

    return answer