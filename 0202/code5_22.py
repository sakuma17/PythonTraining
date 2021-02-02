def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))

eat('トースト','おにぎり')
print()
eat('おにぎり','トースト','カレーうどん')
print()
eat('トースト')
print()
eat('トースト',dinner='焼きそば')
