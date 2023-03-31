# 1~10까지 정수의 합 출력하기

# sum = 0

# for num in range(1, 11, 1):
#     # sum = sum + num
#     sum += num

# print(f'sum = {sum}')

import math, time

import matplotlib.pyplot as plt

# num = int(input('1부터 값을 순차적으로 더할 마지막 숫자(자연수)를 입력해주세요. '))

x = []  # num
y1 = []  # num에 따른 add함수 시간
y2 = []  # num에 따른 formula함수 시간

def add(num):
    sum = 0
    start = time.time()

    for n in range(1, num):
    # print(num)    # => 계산 시간을 유의미하게 증가시킴
        sum += n

    end = time.time()
    y1.append(end - start)
    # print(f'sum = {sum}')
    # print(f"{end - start: .5f}sec") # .5f는 소수점 5자리까지만 출력하도록 함

def formula(num):
    start = time.time()

    sum = (num * (num - 1)) // 2


    end = time.time()
    y2.append(end - start)
    # print(f'sum = {sum}')
    #print(f"{end - start: .5f}sec")

until = 100000
for num in range(until):
    x.append(num)
    print(num)
    add(num)
    # print("------------------------")```
    formula(num)
z = []
for i in range(until):
    z.append(y2[i] - y1[i])

# plt.plot(x, y1, color = 'red')
# plt.plot(x, y2, color = 'blue')
plt.plot(x, z)
plt.show()