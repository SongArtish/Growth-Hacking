num = 1
sum = 0

while num < 11:
    sum += num
    if sum >= 30:
        print(f'num: {num}')
        break
    num += 1