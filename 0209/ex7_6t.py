import random
print('数あてゲームを始めます。3桁の数をあててください')
answer=[random.randint(0,9) for i in range(3)]
prediction=[None for i in range(3)]
print(answer)
while True:
	hit=ball=0
	for i in range(3):
		prediction[i]=int(input(f'{i+1}桁目の予想を入力(0-9)>>'))
		for j in range(3):
			if answer[j]==prediction[i]:
				if i==j:
					hit+=1
				else:
					ball+=1
	print(f'{hit}ヒット!{ball}ボール')
	if hit==3:
		print('正解です!')
		break
	else:
		select=int(input('続けますか?1:続ける 2:終了>>'))
		if select == 2:
			print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした!')
			break
