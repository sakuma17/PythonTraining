food='カツカレー'
if 'カレー' in food:
    print('カレーが含まれています')

food2='すし'
if not 'カレー' in food2:
    print('カレーが含まれていません')

if 'カレー' not in food2:
    print('カレーが含まれていません')

#Pythonでは範囲指定ができる
score=80
if 60<score<80:
    pass

isError=False
n=50

if isError and n<100:
    pass

num=10
if num%2==0:
    print('偶数')
else:
    print('奇数')

aisatsu='さようなら'
if aisatsu=='こんにちは':
    print('ようこそ')
elif aisatsu=='景気は?':
    print('ぼちぼちです')
elif aisatsu=='さようなら':
    print('お元気で！')
else:
    print('どうしました？')

month=int(input('今は何月ですか?(数字を入力)>'))
if month in[1,3,5,7,8,10,12]:
    print('31日までありますね')
else:
    if month!=2:
        print('30日までありますね')
    else:
        print('1年で一番寒い月ですね')
    print('年が明けてから')
print('{}カ月経ちました'.format(month))

number=10
div='偶数' if number%2==0 else'奇数'
print(div)

result='優' if score>=80 else '良' if score>=60 else '可' if score>=40 else '不可'
print(result)
