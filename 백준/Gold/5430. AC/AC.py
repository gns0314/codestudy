from collections import deque

Num = int(input())

for _ in range(Num):
    test = input()
    testNum = int(input())
    if testNum != 0:
        array = deque(map(int, input().strip()[1:-1].split(',')))
    else:
        input()  # 빈 배열 `[]`을 입력 받음
        array = deque()
    
    reverse_flag = False
    error = False
    
    for i in test:
        if i == 'R':
            reverse_flag = not reverse_flag
        elif i == 'D':
            if array:
                if reverse_flag:
                    array.pop()
                else:
                    array.popleft()
            else:
                print('error')
                error = True
                break
    
    if not error:
        if reverse_flag:
            array.reverse()
        print(f"[{','.join(map(str, array))}]")
