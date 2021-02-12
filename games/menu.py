from random import randint
menu_dict={'うどん':200,'ペペロンチーノ':280,'かつ丼':320,'味噌ラーメン':300}
menu_list=['うどん','ペペロンチーノ','かつ丼','味噌ラーメン']

def print_menu():
    print()
    print('メニュー表')
    for i in range(len(menu_list)):
        print(f'{i} {menu_list[i]} {menu_dict[menu_list[i]]}円')

def update_menu_list(num):
    menu_list.pop(num)

money=randint(1000,2000)
while len(menu_list)!=0:
    print_menu()
    print()
    print(f'所持金{money}円')
    num=int(input('購入したいメニューを入力してください>>'))
    if num>len(menu_list)-1:continue
    if menu_dict[menu_list[num]]>money:
        print('所持金が足りません')
        continue
    print(f'{menu_list[num]}を購入しました')
    money-=menu_dict[menu_list[num]]
    update_menu_list(num)
    if money==0:
        print('所持金が無くなりました')
        break
    if min(menu_dict.values())>money:
        print('所持金で購入できるものがありません')
        break
else:
    print()
    print('全て売り切れました')
