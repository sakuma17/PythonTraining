import string
letters=string.ascii_letters

width=int(input('幅>>'))
row_list=list()
for i in range(0,len(letters),width):
    chars=letters[i:i+width]
    print(chars)
    row_list.append(chars)
print()
row=int(input(f'何行目(1~{len(row_list)})>>'))-1
print(row_list[row])
"""
count=0
for char in letters:
    print(char,end='')
    count+=1
    if count%width==0:print()

for i in range(len(letters)):
    print(letters[i],end='')
    if(i+1)%width==0:
        print()

for i,c in enumerate(letters,1):
    print(c,end='')
    if i%width==0:
        print()
"""
