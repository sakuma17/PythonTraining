import tkinter as tk
import datetime as dt
import random
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

def result():
    month=entry1.get().zfill(2)
    day=entry2.get().zfill(2)
    birth=int(month+day)
    today=int(dt.date.today().strftime("%m%d"))
    my_zodi=zodiac(birth)
    now_zodi=zodiac(today)
    result1['text']=f'{my_zodi}座のあなたの運勢は...'
    result1.update()
    result2['text']=fortunes[random.randint(0,2 if my_zodi==now_zodi else 3)]
    result2.update()

root=tk.Tk()
root.title('星座別運勢占い')
root.geometry('250x200')
root.resizable(False,False)
root.configure(bg='skyblue')
label1=tk.Label(root,text='月',bg=root['bg'])
label1.place(x=10,y=0)
entry1=tk.Entry(width=20)
entry1.place(x=10,y=20)
label2=tk.Label(root,text='日',bg=root['bg'])
label2.place(x=10,y=40)
entry2=tk.Entry(width=20)
entry2.place(x=10,y=60)
button=tk.Button(text='占う',command=result)
button.place(x=10,y=85)
result1=tk.Label(root,text='',bg=root['bg'])
result1.place(x=10,y=120)
result2=tk.Label(root,text='',bg=root['bg'])
result2.place(x=10,y=150)
root.mainloop()
