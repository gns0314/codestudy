def solution(arr):
    new_arr = arr[:] 
    visited = {tuple(new_arr): 0}
    for i in range(1, 100): 
        for j in range(len(arr)):
            if new_arr[j] >= 50 and new_arr[j] % 2 == 0: 
                new_arr[j] //= 2
            elif new_arr[j] < 50 and new_arr[j] % 2 == 1:
                new_arr[j] = new_arr[j] * 2 + 1
        if tuple(new_arr) in visited: 
            return i - 1
        visited[tuple(new_arr)] = i