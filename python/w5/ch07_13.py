temp = 30.0

target = int(input("희망 온도를 입력하세요: "))

while temp >= target:
    temp -= 0.1
    result = format(temp, '.2f')
    print(f'현재 온도: {result}')

print('냉방 기능 종료!')