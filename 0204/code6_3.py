"""
userinfo=input('名前と血液型をカンマで区切って1行で入力>>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
print('{}型の{}さんは大吉です'.format(blood,name))
"""

print('{:.1f}'.format(2.345))

l1=['3','5','6']
print('&'.join(l1))

nums='1787942197'
print(nums.count('1'))
print(nums.replace('1','p'))

#helloを1文字ずつ出力
for s in 'hello':
    print(s,end=",")
print()

for i,s in enumerate('hello',1):
    print('{}文字目は{}です'.format(i,s))

s1='hello'
s2=list(reversed(s1))
print(s2)
print(''.join(s2))

#::範囲指定無し -1逆順
s3=s1[::-1]
print(s3)
print(len(s3))
