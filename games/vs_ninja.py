from random import randint

war_num=4
ninja_total=4
ninja_posi=[randint(1,ninja_total) for _ in range(war_num)]
hit=0
blow=0
print('ニンジャが現れ、分身した!')
while hit!=war_num:
    #print(ninja_posi)
    hit=0
    blow=0
    select=input('戦う(nで終了)Enter>>')
    if select=='n':
        print(f'実体は{ninja_posi}だった。戦士たちは力尽きた...')
        break
    for i in range(war_num):
        attack=int(input(f'戦士{i+1}:どのニンジャを攻撃する?(1~{ninja_total})>>'))
        wor_hit=0
        wor_blow=0
        for j in range(len(ninja_posi)):
            if attack==ninja_posi[j]:
                if i==j:
                    wor_hit=1
                    break
                else:
                    wor_blow=1
        if wor_hit==1:
            wor_blow=0
        hit+=wor_hit
        blow+=wor_blow
    print(f'{hit}体の戦士が攻撃を当てた!')
    if hit!=war_num:print(f'{blow}体の戦士が気配を感じた!')
else:
    print('ニンジャの討伐に成功した!!')
