import pprint
x=[n for n in range(1,8)]
print(x)

x=[n**2 for n in range(1,8)]
print(x)

x=[n for n in range(1,8) if n%2==0]
print(x)

# 先に値の式 続いてfor文
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)

# 後ろに外側の要素
x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)

list_j=[[i+j for j in range(1,11)]for i in range(0,100,10)]
pprint.pprint(list_j)
