import random
medal=['鉄十字勲章','騎士鉄十字勲章','柏葉付騎士鉄十字勲章','柏葉・剣付騎士鉄十字勲章','柏葉・ 剣・ダイヤモンド付騎士鉄十字勲章','黄金柏葉・剣・ダイヤモンド付騎士鉄十字勲章']
days=100
defeat=0
hos_days=0

for i in range(days):
    print('{}日目の行動'.format(i+1))
    if hos_days!=0:
        print(f'あと{hos_days}日の入院が必要です')
        hos_days-=1
        input('今はゆっくり休んでくださいね(Enter)')
    else:
        print('出撃!!')
        today_defeat=random.randint(1,15)
        print(f'戦況報告:{today_defeat}輌の戦車を撃破しました!')
        defeat+=today_defeat
        event_num=random.randint(1,100)
        if event_num==100:
            print('あなたは戦死してしまいました...')
            break
        elif event_num>=90:
            hos_days=6
            print(f'あなたは撃墜され、怪我をしてしまいました。{hos_days}日間の入院が必要です')
            input('今は休んでくださいね(Enter)')
        else:
            input('明日も頑張りましょう!(Enter)')
else:
    print('戦争は終結しました!!')
index=defeat//100
print(f'最終戦果報告!!あなたは{defeat}輌の戦車を破壊した功績により{medal[index]}を授与されました!!')
