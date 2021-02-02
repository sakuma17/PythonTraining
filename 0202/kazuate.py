import random
ans=random.randint(1,100)
# randomintは第2引数も含む(以下)
print('1~100の数字の中から一つ選んだよ。')
print('その数字を5回以内に当ててね。')

max_count=5

for i in range(1,max_count+1):
    print(i,'回目、いくつかな?')
    num=int(input())
    if num==ans:
        print('当たり!')
        break
    elif i==max_count:
        pass
    elif num>ans:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
else:
    print('残念~正解は',ans,'でした')
