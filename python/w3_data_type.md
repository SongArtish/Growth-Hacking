# Python과 자료형

## 데이터

모든 데이터는 "메모리"에 저장됨 -> 언제든지 CRUD 할 수 있음

## 변수

- 메모리 주소
- 변수: 메모리 변수에 부여한 이름

```python
# 변수 할당하기 - 여기서 '='은 할당연산자!
myAlphabet = 'A'
```

## 변수명 규칙

- 변수 할당 시 영문자 사용하기!
- 클래스명은 대문자로, 변수명은 소문자로 시작하기!
- 데이터 의미 파악하기 쉽게 작성하기!
- `camelCase` 사용하기!
- 예약어는 변수명으로 사용 X
    ```python
    import keyword
    print(keyword.kwlist)
    ```
- 언더바(`_`) 제외 특수문자는 사용할 수 없음
- 숫자는 첫 글자에서 사용 X

## 입력 받은 데이터 저장하기

```python
userData = input("Please enter the data.")
print(userData)
```

- `input()` 함수로 입력받은 데이터는 무조건 문자열로 처리된다.