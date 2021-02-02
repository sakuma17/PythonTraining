tuple1=(3,5,7)

print(len(tuple1))
print(tuple1[1])
print(sum(tuple1))
list1=list(tuple1)
print(list1)
list1.append(10)
print(list1)

a,b,c=tuple1 #a=3,b=5,c=7
print(a,b,c)

#アンパック代入
x,y=10,20
#2値の入れ替えも一文で可能
x,y=y,x
print(x,y)
