import random

print('数当てゲームを始めます。3桁の数を当ててください!')
select=1
answer=list()
for i in range(3):
    answer.append(random.randint(0,9))
#print(answer)
while select!=2:
    prediction=list()
    hit=0
    ball=0
    print()
    for i in range(len(answer)):
        num=int(input(f'{i+1}桁目の予想を入力(0~9)>>'))
        prediction.append(num)
    for i in range(len(answer)):
        if prediction[i]==answer[i]:
            hit+=1
        for j in range(len(answer)):
            if prediction[j]==answer[i]:
                if prediction[i]!=answer[i]:
                    ball+=1
                    if hit+ball>3:ball=3-hit
    print(f'{hit}ヒット！{ball}ボール！')
    if hit==3:
        print('正解です!')
        break
    select=int(input('続けますか? 1:続ける 2:終了>>'))
