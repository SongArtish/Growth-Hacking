age = int(input("만 나이를 입력하세요: "))
endBirthYear = int(input("출생 연도 끝자리를 입력하세요: "))

if age >= 65:
    print('언제든지 구매 가능합니다.')
elif endBirthYear == 1 or endBirthYear == 6:
    print('월요일에 구매 가능합니다.')
elif endBirthYear == 2 or endBirthYear == 7:
    print('화요일에 구매 가능합니다.')
elif endBirthYear == 3 or endBirthYear == 8:
    print('수요일에 구매 가능합니다.')
elif endBirthYear == 4 or endBirthYear == 9:
    print('목요일에 구매 가능합니다.')
else:
    print('금요일에 구매 가능합니다.')