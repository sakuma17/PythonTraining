count=0
while True:
    count+=1
    print('ひつじが{}匹'.format(count))
    key=input('もう眠りそうですか?(y/n)>')
    if key=='y':
        break
print('おやすみなさい')
