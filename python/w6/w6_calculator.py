class Calculator:
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        return self.n1 + self.n2
    
    def substract(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
    
    def divide(self):
        return self.n1 / self.n2

def printError():
    print("----------------------------------------------")
    print("이 연산에는 오류가 있습니다.")

print("이 계산기는 add/sub/mul/div 연산이 가능합니다.")
print("----------------------------------------------")
operation = input("띄워쓰기를 포함해 연산을 입력하세요: ").split()

result = int(''.join(operation[0]))
op = 0  # 연산자
isError = False

for c in operation[1::]:
    # i) 숫자인 경우
    if op:
        try: int(c)
        except ValueError: isError = True; printError(); break
        num = int(c)
        if op == 1: result += num
        elif op == 2: result -= num
        elif op == 3: result *= num
        elif op == 4: result /= num
        else: isError = True; printError(); break
        op = 0
    # ii) 연산인 경우
    else:
        if c == "+": op = 1
        elif c == "-": op = 2
        elif c == "*": op = 3
        elif c == "/": op = 4
        else: isError = True; printError(); break

if not isError:
    print("----------------------------------------------")
    print(f'계산 결과입니다: {result}')