from random import randint
tp=randint(1,9)
list=list()
for i in range(9):
    if i==(tp)-1:
        list.append('当たり')
    else:
        list.append('ハズレ')
#print(list)
count=0
print('***宝探し***')
while True:
    for i in range(3):
        for j in range(3):
            if list[(i*3+j)]=='選択済みの場所':
                print('x',end='')
            else:
                print(i*3+j+1,end='')
        print()
    select=int(input('好きな数字を選んで入力してください>>'))
    count+=1
    if select==tp:
        print('お宝を見つけました!')
        print(f'あなたはお宝を{count}回で発見しました!')
        break
    else:
        print(f'{list[select-1]}です',end='')
        if list[select-1]=='ハズレ':
            list[select-1]='選択済みの場所'
            msg='大きな' if select<tp else '小さな'
            print(f'。ここより{msg}数字の場所にあります',end='')
        print(),print()
