# 한번더 봐야할 함수식

## 최대공약수를 구하는 함수
```def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return ```
 ## 최소공배수를 구하는 함수
 ```lcd = a * b / find_gcd```
