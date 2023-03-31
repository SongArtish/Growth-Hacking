height = int(input("나무의 높이를 입력하세요: "))

for n1 in range(height+1):
    cntLeaf = n1*2 - 1
    cntBlank = (height * 2 - cntLeaf) // 2
    for _ in range(cntBlank):
        print(' ', end="")
    for _ in range(cntLeaf):
        print("*", end="")
    print()