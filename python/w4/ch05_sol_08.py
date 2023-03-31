myMoney = 5000000
rate = 0.05

for _ in range(5):
    myMoney += myMoney * rate
print(f'5년 후 총 수령액: {round(myMoney)}원')