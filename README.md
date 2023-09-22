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
# 콜라츠의 추측
### 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
```
def solution(n):
    answer = [n]
    while(n > 1):
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer
```
## index() 메소드는 대소문자를 구별하기 때문에, "Kim"이든 "kim"이든 "KIM"이든 "kIm"이든 상관없이 해당 문자열을 찾아줍니다.

# 투포인터 알고리즘 
```
def solution(n):
    answer = 0
    left, right, cnt = 0,0,0

    while left < n:
        if cnt < n:
            right += 1
            cnt += right
        else:
            if n == cnt: answer += 1
            left += 1
            cnt -= left

    return answer
```
