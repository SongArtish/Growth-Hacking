# 객체 지향 프로그래밍

> OOP(Object Oriented Programming)

## Object

- `사물`을 의미
- **속성**(attribute: 객체를 구성하는 요소)과 **기능**(function: 객체가 하는 행위)으로 구성됨

### `__init__()` Method

- `__init__()` method는 객체를 메로리에 할당하여 생성하는 기능을 담당함(생성자 호출)

### 도트 연산자(`.`)

- 객체의 메서드를 호출하기 위해 도트 연산자(`.`)를 이용함
- 속성에 접근할 수 있으니 변경도 가능함
    ```python
    class Calculator:
        def __init__(self, n1, n2):
            self.num1 = n1
            self.num2 = n2
        pass
    clac1 = Calculator(10, 20)

    # 직접 접근해서 변경이 가능함
    calc1.num1 = 100
    ```