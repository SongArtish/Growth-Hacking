def greets(countryCode):
    if countryCode == "1":
        print('안녕')
    elif countryCode == "3":
        print('こんにちは')
    else:
        print('Hello')

countryCode = input('where are you from? 1. 한국, 2. USA, 3. Japan')
greets(countryCode)