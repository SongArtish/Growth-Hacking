import convertUnitModule as cu

inputData = int(input('길이(mm)를 입력하세요.'))

result = cu.convertUnit(inputData)
cu.printLength(inputData, result)