import tkinter
root=tkinter.Tk()
root.geometry('300x200')

label_a=tkinter.Label(root.text='Hello everybody',bg='yellow',relief=tkinter.RIDGE,bd=2)
label_a.place(x=10,y=10)

label_b=tkinter.Label(root.text='Oh My God!',bg='red')
label_b.place(x=10,y=30)

label_c=tkinter.Label(root.text='See you tomorrow',bg='LightSkyBlue')
label_b.place(x=30,y=50)

root.mainloop()
