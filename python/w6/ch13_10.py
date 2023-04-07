file = open('./number.txt', 'w')
file.write('123')
file.close()

file = open('./number.txt', 'r')
result = file.read()
sum = int(result) + 877
print(sum)