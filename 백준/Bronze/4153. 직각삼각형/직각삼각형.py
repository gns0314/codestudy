while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break
    b = [i * i for i in a]
    b.sort()
    if b[0] + b[1] == b[2]:
        print('right')
    else:
        print('wrong')
