import random
import datetime
fortunes=['大吉','中吉','小吉','凶']

def zodiac(birth):
    zodi=''
    if birth>=1222 or 101<=birth<=119:
        zodi='やぎ'
    elif birth>=1123:
        zodi='いて'
    elif birth>=1024:
        zodi='さそり'
    elif birth>=923:
        zodi='てんびん'
    elif birth>=823:
        zodi='おとめ'
    elif birth>=723:
        zodi='しし'
    elif birth>=622:
        zodi='かに'
    elif birth>=521:
        zodi='ふたご'
    elif birth>=420:
        zodi='おうし'
    elif birth>=321:
        zodi='おひつじ'
    elif birth>=219:
        zodi='うお'
    elif birth>=120:
        zodi='みずがめ'
    return zodi

def result(birth,today):
    my_zodi=zodiac(birth)
    now_zodi=zodiac(today)
    msg=f'{my_zodi}座のあなたの運勢は...'
    fortune=fortunes[random.randint(0,2 if my_zodi==now_zodi else 3)]
    print(msg)
    print(fortune)

month=input('月').zfill(2)
day=input('日').zfill(2)
birth=int(month+day)
today=int(datetime.date.today().strftime("%m%d"))
result(birth,today)
