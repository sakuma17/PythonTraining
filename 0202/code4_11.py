ages=[28,50,'秘密',20,78,25,22,'無回答',10,33]
samples=list()
for data in ages:
    if not isinstance(data,int):
        continue
    if data<20 or data>=30:
        continue
    samples.append(data)
print(samples) 
