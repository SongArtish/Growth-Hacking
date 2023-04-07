def print_error():
    print("----------------------------------------------")
    print("이 연산에는 오류가 있습니다.")

def calculate(operation):
    result = float(operation[0])
    op = 0  # 연산자
    is_error = False

    for c in operation[1::]:
        # i) 숫자인 경우
        if op:
            try: num = float(c)
            except ValueError: is_error = True; print_error(); break
            if op == 1: result += num
            elif op == 2: result -= num
            elif op == 3: result *= num
            elif op == 4:
                if num == 0: is_error = True; print_error(); break
                result /= num
            else: is_error = True; print_error(); break
            op = 0
        # ii) 연산인 경우
        else:
            if c in ["+", "-", "*", "/"]: op = ["+", "-", "*", "/"].index(c) + 1
            else: is_error = True; print_error(); break

    if not is_error:
        print("----------------------------------------------")
        print(f'계산 결과입니다: {result}')

print("이 계산기는 add/sub/mul/div 연산이 가능합니다.")
print("----------------------------------------------")
while True:
    operation = input("띄워쓰기를 포함해 연산을 입력하세요: ").split()
    if operation[0].lower() == "quit": break
    calculate(operation)