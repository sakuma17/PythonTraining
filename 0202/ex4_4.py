for i in range(1,10):
    for j in range(1,10):
        if j==9:
            print(f'{i*j}')
        else:
            print(f'{i*j},',end='')
print('')

"""
for i in range(1,10,2):
    for j in range(1,10):
        if j==9:
            print(f'{i*j}')
        else:
            print(f'{i*j},',end='')
    print('')
"""
for i in range(1,10):
    if i%2==0:
        continue
    for j in range(1,10):
        if j==9:
            print(f'{i*j}')
        else:
            print(f'{i*j},',end='')

print('')

for i in range(1,10,2):
    for j in range(1,10):
        if ((i*j)>50) or (j==9):
            print(f'{i*j}')
            break
        else:
            print(f'{i*j},',end='')
