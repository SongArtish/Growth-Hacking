# 파일 쓰기

file = open('./test.txt', 'w')
result = file.write('Hello python!')

print(f'type of result: {type(result)}')    # type of result : <class 'int'>
print(f'result: {result}')  # result : 13

file.close()

# ------------------------

# file = open('C:\python\test.txt', 'r')
# result = file.read()
# print(f'type of result: {type(result)}') 
# print(f'result: {result}')

# file.close()