def add():
    print('덧셈 결과: ', num1 + num2)

def sub():
    print('뺄셈 결과: ', num1 - num2)

def mul():
    print('곱셈 결과: ', num1 * num2)

def div():
    print('나눗셈 결과: ', num1 / num2)

def calculator():
    if(selectOperator == 1):
        add()
    elif(selectOperator == 2):
        sub()
    elif(selectOperator == 3):
        mul()
    elif(selectOperator == 4):
        div()
    else:
        print('Something went wrong.')

# 입력 숫자는 실수가 올 수 있기 떄문에, int가 아닌 float로 형변환해주어야 함!
num1 = float(input('숫자를 입력하세요. '))
selectOperator = int(input('연산자를 선택하세요. 1. 뎃셈, 2. 뺼셈, 3. 곱셈, 4.나눗셈 '))
num2 = float(input('숫자를 입력하세요. '))

calculator()