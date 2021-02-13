import tkinter as tk
def calc_payment():
    fee=int(entry1.get())
    people=int(entry2.get())
    dnum=fee/people
    pay=int(dnum//100*100)
    if dnum>pay:
        pay+=100
    payorg=fee-pay*(people-1)
    result['text']=f'1人あたり{pay}円({people-1}人)、幹事は{payorg}円です'
    result.update()
root=tk.Tk()
root.title('割り勘くん')
root.geometry('250x200')
root.resizable(False,False)
root.configure(bg='skyblue')
label1=tk.Label(root,text='金額',bg=root['bg'])
label1.place(x=10,y=0)
entry1=tk.Entry(width=20)
entry1.place(x=10,y=20)
label2=tk.Label(root,text='人数',bg=root['bg'])
label2.place(x=10,y=40)
entry2=tk.Entry(width=20)
entry2.place(x=10,y=60)
button=tk.Button(text='計算する',command=calc_payment)
button.place(x=10,y=85)
result=tk.Label(root,text='',bg=root['bg'])
result.place(x=10,y=120)
root.mainloop()
