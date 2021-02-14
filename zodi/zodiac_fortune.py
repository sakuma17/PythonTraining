import tkinter as tk
import datetime as dt
import random
fortunes=['大吉','中吉','小吉','凶']

def zodiac(birth):
    zodi=''
    if 1231>=birth>=1222 or 119>=birth>=101:
        zodi='やぎ'
    elif 1221>=birth>=1201 or 1130>=birth>=1123:
        zodi='いて'
    elif 1122>=birth>=1101 or 1031>=birth>=1024:
        zodi='さそり'
    elif 1023>=birth>=1001 or 930>=birth>=923:
        zodi='てんびん'
    elif 922>=birth>=901 or 831>=birth>=823:
        zodi='おとめ'
    elif 822>=birth>=801 or 731>=birth>=723:
        zodi='しし'
    elif 722>=birth>=701 or 630>=birth>=622:
        zodi='かに'
    elif 621>=birth>=601 or 531>=birth>=521:
        zodi='ふたご'
    elif 520>=birth>=501 or 430>=birth>=420:
        zodi='おうし'
    elif 419>=birth>=401 or 331>=birth>=321:
        zodi='おひつじ'
    elif 320>=birth>=301 or 229>=birth>=219:
        zodi='うお'
    elif 218>=birth>=201 or 131>=birth>=120:
        zodi='みずがめ'
    else:
        zodi='不明'
    return zodi

def result():
    month=entry1.get().zfill(2)
    day=entry2.get().zfill(2)
    birth=int(month+day)
    today=int(dt.date.today().strftime("%m%d"))
    my_zodi=zodiac(birth)
    if my_zodi=='不明':
        result1['text']='存在する日付を'
        result2['text']='入力してください'
    else:
        now_zodi=zodiac(today)
        index=(birth+today)%4
        if my_zodi==now_zodi and index>0:
            index-=1
        result1['text']=f'{my_zodi}座のあなたの運勢は'
        result2['text']=fortunes[index]
    result1.update()
    result2.update()

root=tk.Tk()
root.title('占い')
root.geometry('200x200')
#root.resizable(False,False)
root.configure(bg='pink')

label=tk.Label(root,text='今日の運勢占い',bg=root['bg'],font=('MS ゴシック',14,'bold'),fg='white')
label.place(x=20,y=10)

nolabel=tk.Label(text='',bg=root['bg'])
nolabel.grid(row=0,column=0,pady=10)

nolabel0=tk.Label(text='',bg=root['bg'])
nolabel0.grid(row=1,column=0)
nolabel1=tk.Label(text='        ',bg=root['bg'])
nolabel1.grid(row=1,column=1)
label0=tk.Label(root,text='誕生日:',bg=root['bg'])
label0.grid(row=1,column=2)
entry1=tk.Entry(width=2)
entry1.grid(row=1,column=3,padx=5,pady=5)
label1=tk.Label(root,text='月',bg=root['bg'])
label1.grid(row=1,column=4,sticky=tk.W)
entry2=tk.Entry(width=2)
entry2.grid(row=1,column=5,sticky=tk.W)
label2=tk.Label(root,text='日',bg=root['bg'])
label2.grid(row=1,column=6,sticky=tk.W)

button=tk.Button(text='占う',command=result)
button.place(x=85,y=77)
result1=tk.Label(root,text='',bg=root['bg'])
result1.place(x=37,y=107)
result2=tk.Label(root,text='',bg=root['bg'])
result2.place(x=37,y=137)

root.mainloop()
