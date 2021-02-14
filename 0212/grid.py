import tkinter
root=tkinter.Tk()
root.geometry('300x200')

label_a=tkinter.Label(root,text='Hello everybody',bg='yellow',relief=tkinter.RIDGE,bd=2)
label_a.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

label_b=tkinter.Label(root,text='Oh My God!',bg='red')
label_b.grid(row=1,column=0,padx=5,pady=5)

label_c=tkinter.Label(root,text='See you tomorrow',bg='LightSkyBlue')
label_c.grid(row=1,column=1,padx=5,pady=5)

root.mainloop()
