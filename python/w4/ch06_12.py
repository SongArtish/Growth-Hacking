num = int(input('자연수를 입력하세요.'))

if num > 0:
    if num % 2 == 0:
        print(f'{num}은 짝수')
    else:
        print(f'{num}은 홀수')  
else:
    print(f'{num}은 자연수가 아닙니다.')