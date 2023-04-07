# 컨테이너 자료형

- '데이터 집합체'
- 데이터를 하나씩 저장하여 사용하기보다 여러 데이터를 묶어서 저장/관리하여 효율적으로 사용
- Python에서 제공하는 컨테이너 자료형으로는 **리스트(list)**, **튜플(tuple)**, **딕셔너리(dictionary)**가 있음



## 1. List

- 같은 유형의 데이터를 나열한 것
- 어떤 데이터 집합을 순차적으로 나열하고자 할 때 사용
- 리스트 내 데이터는 메모리의 연속된 공간에 순서대로 저장됨



### 1.1 리스트 선언

- 대괄호(`[]`)를 이용해 데이터를 묶고, 데이터와 데이터는 쉼표(`,`)로 구분함
- 리스트 출력
    - Shell 모드
        ```python
        fruits = ['사과', '포도', ...]
        fruits
        ```
    - 코드 편집기
        ```python
        print(fruits)
        ```



### 1.2 리스트 조회

- 반복문을 이용해 리스트 전체를 조회할 수 있음
    ```python
    balls = [...]
    
    for ball in balls:
        print(f'ball: {ball}')

    # enumerate() 함수
    for index, ball in enumerate(balls):
        print(f'index: {index}, ball: {ball}')
    ```



### 1.3 인덱스 조회

- `index()` 함수를 사용함
- 조회하려는 아이템으 2개 이상인 경우 가장 앞에 있는 아이템의 인덱스 값이 출력됨
- `index()` 함수는 문자열(string)에서 특정 문자나 특정 문자열의 위치를 찾을 때도 사용이 가능!
    (단 찾는 문자열이 없는 경우 에러 발생)



### 1.4 아이템 삽입

- `append()` 함수
    - 리스트 끝에 아이템을 추가하는 함수
- `insert()` 함수
    - 특정 위치에 아이템을 삽입하는 함수

    ```python
    LIST.insert(삽입할 위치의 인덱스, 삽입할 아이템 값)
    ```



### 1.5 리스트 연결

- `extend()` 함수 사용
- 리스트에 또 다른 리스트를 연결

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)
# 혹은
list1 = list1 + list2
```



### 1.6 아이템 삭제

- `pop()` 함수
    a. 괄호를 빈 채로 두면, 리스트 맨 끝의 아이템을 삭제
    b. 괄호 안에 삭제할 인덱스를 넣으면, 그 인덱스에 있는 아이템 삭제
    -  실행 결과로 삭제된 아이템을 반환함

    ```python
    sports = [...]
    sports.pop()
    sports.pop(2)   # 인덱스가 '2'인 아이템 삭제
    ```

- `del` 키워드
    - `del` 키워드를 이용해서 특정 위치 아이템을 삭제할 수도 있음

    ```python
    sports = [...]
    del sports[2]   # 인덱스가 '2'인 아이템 삭제
    ```

- `remove()` 함수
    - 특정 아이템 삭제
    - 매개변수로 삭제하고자 하는 아이템을 넣어주면 삭제됨
    - 리스트에 삭제할 아이템이 여러 개 있는 경우, 가장 앞에 있는 아이템이 삭제됨

    ```python
    languages = [...]
    languages.remove('java')
    ```

    - 만약 특정 아이템 여러 개를 모두 찾아서 삭제하는 경우, 반복문을 사용하면 됨!



### 1.7 리스트 정렬, 역정렬, 슬라이싱

- `sort()` 함수
    
    ```python
    numbers = [5, 1, 3, 4, 2, 6]

    numbers.sort()  # 기본 옵션은 reverse = False
    numbers.sort(reverse = False)   # 오름차순 정렬
    numbers.sort(reverse = True)    # 내림차순 정렬
    ```

- `reverse()` 함수
    - 아이템을 역순으로 뒤집는 함수

    ```python
    vegetables = ['carrot', 'cucumber', 'onion', 'potato', 'sweat potato']
    vegtetables.reverse()   # 리스트 순서 뒤집기
    ```

- 슬라이싱
    - 리스트에서 필요한 부분의 아이템만 뽑아내는 것
    - `[n:m]`: n 인덱스부터 (m-1) 인덱스까지의 아이템을 슬라이싱(추출)함
    - 위에서 n을 생략하면 0부터, m을 생략하면 리스트 맨 끝 아이템까지 추출함



## 2. Tuple



## 3. Dictionary