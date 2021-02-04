import random
bingo=[[random.randint(0,9) for j in range(3)]for i in range(3)]
for row in bingo:
    print(row)

vertical=[[bingo[j][i] for j in range(3)]for i in range(3)]
for row in vertical:
    print(row)

cross=[[bingo[j][j] if i==0 else bingo[j][2-j] for j in range(3)]for i in range(2)]
for row in cross:
    print(row)
