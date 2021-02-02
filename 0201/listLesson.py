list1=[] #空のリスト
list2=list() #同上

list1.append(3)
print(list1)
list1.append(5)
print(list1[1])

list2.append(10)
list2.append(20)
print(list2)

list3=list1+list2
print(list3)

list4=list3*3
print(list4)

print(len(list4)) #list4の要素数
print(sum(list4)) #list4の中身の合計

del list4[0] #インデックス0の要素を削除
print(list4)

list4.remove(5) #list4内の最初の5の要素を削除
print(list4)

list5=list4[3:8] #list4のインデクックス3以上8未満
print(list5)

print(list5[-1]) #listの最後の要素
