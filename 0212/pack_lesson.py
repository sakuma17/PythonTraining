# https://pg-chain.com/python-pack-grid-place
import tkinter
#画面
root=tkinter.Tk()
root.geometry('300x200')
#ボタン
btn=tkinter.Button(root,text='終了')
#配置
btn.pack(fill='x',pady=10,padx=30,ipady=10)

root.mainloop()
