# 반복문



## 반복문 종류

- **for문**: <u>지정된 횟수</u>에 따라 반복
- **while문**: <u>조건식의 결과가 참</u>일 때 반복



## for문

```python
for i in range(1, 11, 1):
    print(i)
```
- **iterable**: '반복 가능한 객체'를 의미하며, `range()` 함수를 이용해 범위 설정
- **item**: iterable의 데이터를 순차적으로 저장하는 변수



### 문자열을 이용한 for문

- 이터러블에 문자열을 넣으면 item에는 첫 문자부터 끝 문자가 순차적으로 저장됨

```python
for c in 'Hello':
    print(c)
```


# while문

```python
while num < 5:
    print(num)
    num += 1
```



# for문과 while문의 차이점

- 횟수를 중요시하는 반복문은 for문을 사용
- 특정 조건을 중요시하는 반복문은 while문을 사용



# 반복문 내 실행제어

- `continue`: 이후 실행을 생략하고 다시 반복문의 처음으로 돌아감
- `break`: 실행을 중단하고 반복문을 빠져나옴
- `pass`: 반목문 내 실행문이 아직 정해지지 않았을 때 사용(조건문, 반복문, 함수, 클래스 등에서도 사용ㄷ됨)