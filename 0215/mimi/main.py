#https://joytas.net/programming/python/realtime
import tkinter as tk
key=''
#引数イベントオブジェクト
def key_down(e):
    global key
    key=e.keysym
    #e.keysym:押したボタンの名前を教えてくれる

def key_up(e):
    global key
    key=''

cx=400
cy=300

def main_proc():
    global cx,cy
    if key=='Up':
        cy=cy-20
    if key=='Down':
        cy=cy+20
    if key=='Left':
        cx=cx-20
    if key=='Right':
        cx=cx+20
        """
    if key=='r':
        cx=cx+20
        cy=cy+20
        """
    #coordsは表示中の画像を新しい位置に移動する
    canvas.coords('MYCHR',cx,cy)
    root.after(100,main_proc)

root=tk.Tk()
root.bind('<KeyPress>',key_down)#キーが押されたときにkey_down実行
root.bind('<KeyRelease>',key_up)
canvas=tk.Canvas(width=800,height=600,bg='lightgreen')
canvas.pack()
img=tk.PhotoImage(file='mimi.png')
canvas.create_image(cx,cy,image=img,tag='MYCHR')
main_proc()
root.mainloop()
