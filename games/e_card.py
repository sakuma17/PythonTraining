import random
my_cards=['市民' for _ in range(4)]
com_cards=my_cards.copy()
my_cards.append('奴隷')
com_cards.append('皇帝')
"""
print(my_cards)
print(com_cards)
"""
print('ようこそeカードゲームへ')
input('>>enter')
for i in range(5):
    print()
    print(f'{i+1}戦目')
    print(f'手持ちのカード:市民{len(my_cards)-1}枚 奴隷1枚')
    select=input('カード選択:市民なら0、奴隷なら1を入力>')
    my_card=my_cards.pop() if select=='1' else my_cards.pop(0)
    com_card=com_cards.pop(random.randint(0,len(com_cards)-1))
    print()
    print('カードオープン!')
    input('>>enter')
    print()
    print(f'あなた:{my_card} PC:{com_card}')
    if my_card=='市民' and com_card=='市民':
            print('引き分け')
            continue
    elif my_card=='奴隷' and com_card=='皇帝':
            print('あなたの勝ち')
            print('Congratulation!')
    else:
        print('あなたの負け')
        print('GAME OVER')
    break
