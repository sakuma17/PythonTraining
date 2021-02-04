import random
#balls=[i+1 for i in range(99)]
balls=list(range(1,100))
random.shuffle(balls)
a_win=b_win=0
for i in range(5):
    print(f'{i+1}回戦')
    a=balls[i*2]
    b=balls[i*2+1]
    if a>b:
        msg='A'
        a_win+=1
    else:
        msg='B'
        b_win+=1
    print(f'A:{a},B:{b}…{msg}の勝ち')
    print()
winner='A' if a_win>b_win else 'B'
print(f'{max(a_win,b_win)}対{min(a_win,b_win)}で{winner}の勝ち')
