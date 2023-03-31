# x, y = 2, 3
# z = x * y / 2

# while z < 150:
#     print(f'width = {x}, height = {y}. area = {z}')
#     x += 2
#     y += 3
#     z = x * y / 2

count = 1

while True:
    area = ((count * 2) * (count * 3)) / 2
    if area > 150: break
    print(f'width = {count*2}, height = {count*3}. area = {area}')
    count += 1