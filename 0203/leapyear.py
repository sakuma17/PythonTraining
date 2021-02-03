def is_leapyear(year):
    if year%400==0:
        return True
    if year%4==0 and year%100!=0:
        return True
    return False

year=int(input('西暦何年?>'))
if is_leapyear(year):
    print('西暦{}年はうるう年です'.format(year))
else:
    print('西暦{}年はうるう年ではありません'.format(year))
