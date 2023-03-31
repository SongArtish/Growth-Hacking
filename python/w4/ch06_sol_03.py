print('Good morning. Nice to meet you \n Where are you from? \n Please select a number.')
choice = int(input('1. 대한민국 2. USA 3. 中国 4. 日本 '))

if choice == 1:
    print('주문하시겠어요?')
elif choice == 3:
    print('您要点菜吗?')
elif choice == 4:
    print('ご注文なさいますか')
else:
    print('Would you like to order?')
