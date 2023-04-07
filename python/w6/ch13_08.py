file = open('./test.txt', 'r')

result = file.read()

# write하는 경우, result는 문자열 길이를 보여줌
print(f'type of result: {type(result)}')    # type of result : <class 'str'>
print(f'result: {result}')  # result : Hello python!

file.close()