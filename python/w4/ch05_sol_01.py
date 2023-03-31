# Codes
# sales1 = int(input('1월 매출: '))
# sales2 = int(input('2월 매출: '))
# sales3 = int(input('3월 매출: '))
# total = sales1 + sales2 + sales3
# print(f'1분기 전체 매출: {total}원')

# Chat GPT suggestion:
sales = [int(input(f'{i+1}월 매출: ')) for i in range(3)]
total = sum(sales)
print(f'1분기 전체 매출: {total}원')