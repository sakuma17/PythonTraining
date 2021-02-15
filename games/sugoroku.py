import random
point=0
GOAL=15
assets=0

while True:
    select=input('サイコロを振る(nで終了)Enter>')
    if select=='n':break
    forward=random.randint(1,6)
    print(f'{forward}の目が出た。{forward}マス進む')
    point+=forward
    income=random.randrange(-500,1000,100)
    if income>0:
        print(f'ビジネスに成功!{income}万円獲得した')
    elif income<0:
        print(f'ビジネスに失敗!{abs(income)}万円損失した')
    assets+=income
    if point>=15:break
    print(f'現在資産{assets}万円。ゴールまであと{GOAL-point}です')
if point>=15:
    print(f'ゴール!総資産は{assets}万円です')
print('ゲーム終了')
