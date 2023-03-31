# operator 모듈을 연산자를 대신해서 사용할 수 있다!
# operator 모듈을 사용하는 이유?
## -> 가독성을 높이며, 연산 속도가 빨라짐(연산 기호를 사용하면 파이썬 내부에서 기호를 함수로 변환해서 연산을 실행함)
from operator import *
# from operator import add, sub, mul, truediv, mod, floordiv

def p(param):
    print(param)

num1 = 10
num2 = 3

p(add(num1, num2))
p(sub(num1, num2))
p(mul(num1, num2))
p(truediv(num1, num2))
p(mod(num1, num2))
p(floordiv(num1, num2))
p(pow(num1, num2))

p(eq(num1, num2))
p(ne(num1, num2))
p(gt(num1, num2))
p(ge(num1, num2))
p(lt(num1, num2))
p(le(num1, num2))

p(and_(True, False))