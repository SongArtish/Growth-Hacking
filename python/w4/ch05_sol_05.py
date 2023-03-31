# inputData = int(input('손 안에 동전 수를 입력하세요. '))
# result = inputData % 2
# print(result)

# 동전 맞추기 게임
import random
guess = int(input('손 안에 동전이 1개 혹은 2개가 있습니다. 맞춰보세요. '))
result = random.randint(1, 2)
print(f"손 안에 동전 개수는 {result}개였습니다!")
if guess == result:
    print("정답입니다.")
else:
    print("틀렸습니다.")