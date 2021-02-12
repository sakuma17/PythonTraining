# https://pg-chain.com/python-pack-grid-place
import tkinter
#画面
root=tkinter.Tk()
root.geometry('300x200')
#ボタン
btn=tkinter.Button(root,text='開始',width=14)
#btn.pack(fill='x',padx=20,side='left')
btn.pack(fill='x',padx=20,side='top')
#配置
btn2=tkinter.Button(root,text='終了',width=14)
#btn2.pack(fill='x',padx=20,side='left')
btn2.pack(fill='x',padx=20,side='top')

root.mainloop()
