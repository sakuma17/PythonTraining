import tkinter as tk
def bt_click():
    btn['text']='Clicked!!'
root=tk.Tk()
root.title('My Window')
root.geometry('600x400')
"""
label=tk.Label(root,text='Hello,World!',font=('Arial',50))
label.place(x=100,y=100)
"""
btn=tk.Button(root,text='Click Me!',font=('Arial',50),command=bt_click)
btn.place(x=100,y=100)
root.mainloop()
