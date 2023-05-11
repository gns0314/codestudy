def solution(arr):
    new_arr = arr[:] # arr의 값을 복사해서 새로운 리스트를 생성
    visited = {tuple(new_arr): 0} # 방문한 리스트들을 저장하는 딕셔너리 생성, 초기값 0
    for i in range(1, 100): # 최대 100번 반복
        for j in range(len(arr)):
            if new_arr[j] >= 50 and new_arr[j] % 2 == 0: # 50 이상 짝수인 경우
                new_arr[j] //= 2
            elif new_arr[j] < 50 and new_arr[j] % 2 == 1: # 50 미만 홀수인 경우
                new_arr[j] = new_arr[j] * 2 + 1
        if tuple(new_arr) in visited: # 이미 방문한 리스트인 경우
            return i - 1 # 현재 반복 횟수 반환
        visited[tuple(new_arr)] = i # 방문한 리스트에 현재 반복 횟수 저장
    return -1 # 100번 이상 반복한 경우