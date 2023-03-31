# from sys import _getframe as frame

def p(name):
    print(f'{name} 함수를 호출합니다!')

def fun1():
    p('fun1')

def fun2():
    p('fun2')

def fun3():
    fun1()
    fun2()
    p('fun3')

fun3()