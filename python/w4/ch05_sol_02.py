sales = int(input('1분기 매출: '))  # 매출
purchase = int(input('1분기 매입: '))   # 매입
profit = sales - purchase   # 수익
print(f'수익: {profit}원')

# ChatGPT - Descriptive Variable Names
quarterly_sales = int(input('1분기 매출: '))
quarterly_purchases = int(input('1분기 매입: '))
quarterly_profit = quarterly_sales - quarterly_purchases
print(f'1분기 수익: {quarterly_profit:,}원')