def eat(**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key,kwargs[key]))

eat(朝食='納豆',遅めの昼食='パスタ',夕方のおやつ='カレーパン')
"""
eat({'朝食':'納豆','遅めの昼食':'パスタ','夕方のおやつ':'カレーパン'})
"""
