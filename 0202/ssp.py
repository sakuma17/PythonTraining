import random
num_list =list()

for i in range(100):
    num=random.randint(1,100)
    num_list.append(num)

for index in range(len(num_list)): 
    if num_list[index]==77:
        print('77->',index,sep='')
        break
else:
    print('77->なし')

for count in range(len(num_list)):
    print(num_list[count],end='')
    if (count+1)%10!=0:
        print(',',end='')
    else:
        print()
