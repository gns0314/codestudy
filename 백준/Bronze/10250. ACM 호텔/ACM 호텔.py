num = int(input())

for _ in range(num):
    h, w, t = map(int, input().split())

    c = [[0] * w for _ in range(h)]

    tmp = 101
    for i in range(h):
        for j in range(w):
            c[i][j] = tmp + j
        tmp += 100

    row_idx = (t - 1) % h
    col_idx = (t - 1) // h

    # 출력
    print(c[row_idx][col_idx])
