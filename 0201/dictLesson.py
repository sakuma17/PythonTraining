dict1=dict() #空のdict
dict1['apple']='りんご'
dict1['orange']='みかん'
print(dict1)

print(len(dict1))
dict1['banana']='ばなな'

del dict1['orange']
print(dict1)

print(dict1['apple']) # 指定したキーのバリューを取得

#print(dict1['pine']) #無いのでerror
print(dict1.get('pine')) #Noneを返す
print(dict1.get('banana')) #ばなな

if 'apple' in dict1:
    print('key:appleは含まれている')

if 'pine' not in dict1:
    print('key:pineは含まれていない')

if 'りんご' in dict1.values():
    print('value:りんごは含まれている')
