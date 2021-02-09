from random import randint
input('Enterで対決開始')
while True:
    you=list()
    com=list()
    for _ in range(3):
        you.append(randint(1,6))
        com.append(randint(1,6))
    print('あなたの出目')
    print(you)
    print('コンピューターの出目')
    print(com)
    you_score=sum(you)
    if len(set(you))==1:you_score*=2
    com_score=sum(com)
    if len(set(com))==1:com_score*=2
    msg='あいこ' if you_score==com_score else 'あなたの勝ち' if you_score>com_score else 'あなたの負け'
    print(f'{you_score}対{com_score}で{msg}')
    select=input('もう一度対決しますか?<y/n>')
    if select=='n':break
