import random

trial=int(input('100~1000の範囲の偶数をいくつ生成する?>>'))
nums=list()
for _ in range(trial):
    nums.append(random.randrange(100,1000,2))
nums.sort(reverse=True)
print(f'{trial}個生成しました!降順に表示します{nums}')
