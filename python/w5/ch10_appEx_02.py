def calculator(a, b, operator):
    a = float(a)
    b = float(b)
    if operator == "1":
        return a + b
    elif operator == "2":
        return a - b
    elif operator == "3":
        return a * b
    elif operator == "4":
        return a / b
    else:
        print('Invalid input. Please check it again.')

a = input("숫자를 입력하세요.")
operator = input("연산자를 선택하세요. 1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈 ")
b = input("숫자를 입력하세요.")

print(calculator(a, b, operator))