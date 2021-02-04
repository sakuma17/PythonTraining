import random

trial=int(input('サイコロを何回ふる?>>'))
dices=[random.randint(1,6) for _ in range(trial)]
"""
dices=list()
nums=set()
for _ in range(trial):
    num=random.randint(1,6)
    print(num)
    dices.append(num)
    nums.add(num)
"""
print(dices)
print('出た目は{}の{}種類'.format(set(dices),len(set(dices))))
