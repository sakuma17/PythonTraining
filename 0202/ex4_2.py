count=1
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーを食べました')
    ans=input('おかわりはいかがですか?(y/n)>>')
    if ans=='n':
        break
    count+=1
print('ごちそうさまでした')
