# 1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기
for num in range(1, 11, 1):
    print(f'num = {num}')
    if num % 3 == 0:
        print('3의 배수!')