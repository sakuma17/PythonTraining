import random

hands={0:'グー',1:'チョキ',2:'パー'}
while True:
    you=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
    pc=random.randint(0,2)
    print(f'あなたは{hands[you]},PCは{hands[pc]}')
    if you==pc:
        print('あいこ')
        continue
    elif (you-pc+3)%3==2:
        print('あなたの勝ち')
    else:
        print('あなたの負け')
    break
