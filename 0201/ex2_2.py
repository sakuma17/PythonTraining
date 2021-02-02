list=[]
list.append(int(input('国語>')))
list.append(int(input('算数>')))
list.append(int(input('理科>')))
list.append(int(input('社会>')))
list.append(int(input('英語>')))
print('合計点',sum(list),'平均点',sum(list)/len(list))
