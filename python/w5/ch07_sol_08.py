# 0~100까지 정수 중 3과 8의 공배수와 최소공배수 출력

num = 1
minNum = 0

while num <= 100:
    if num % 3 == 0 and num % 8 == 0:
        print(f'공배수: {num}')
        if minNum == 0: minNum = num
    num += 1

print(f'최소공배수: {minNum}')