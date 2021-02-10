from random import randint
menu={'うどん':200,'ペペロンチーノ':280,'かつ丼':320,'味噌ラーメン':300}
list=['うどん','ペペロンチーノ','かつ丼','味噌ラーメン']

def print_menu():
    print('メニュー表')
    for i in range(len(list)):
        print(f'{i} {list[i]} {menu[list[i]]}円')

def update_list(num):
    list.pop(num)

money=randint(1000,2000)
while True:
    print_menu()
    print()
    print(f'所持金{money}円')
    num=int(input('購入したいメニューを入力してください>>'))
    if num==5:break
    print(f'{list[num]}を購入しました')
    money-=menu[list[num]]
    update_list(num)
    if len(list)==0:
        print('全て売り切れました')
        break
    """
    if sum()>money:
        print('購入できるものがありません')
        break
    """
