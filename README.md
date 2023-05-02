# 한번더 봐야할 함수식 or 알고리즘

## 최대공약수를 구하는 함수
```
def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return 
```   
## 최소공배수를 구하는 함수
 ```
 lcd = a * b / find_gcd
 ```

# 그리디 알고리즘(욕심쟁이 알고리즘)
### 입력을 받은 금액을 5000, 1000, 500, 100 원으로 나눠주는 문제( 최적해 문제)

```
def solution(a):
    b = [5000,1000,500,100]
    result = {}             # 딕셔너리 형태로 받아 보기 좋게 결과값 저장 
    for i in b:
        c = a // i
        if c > 0 :
            result[i] = c   # 교환 결과에 해당 동전 개수 추가
            a -= c * i      # 교환한 금액만큼 총액에서 뺌
    return result        

solution(int(input()))

```
