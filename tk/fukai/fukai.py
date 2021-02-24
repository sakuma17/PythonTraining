import tkinter as tk

root=tk.Tk()
root.geometry('400x700')
root.title('不快指数')
root['bg']='skyblue'
f_colors=['#0868af','#04fa76','#ec6941','red']
images=[
        tk.PhotoImage(file='img0.png'),
        tk.PhotoImage(file='img1.png'),
        tk.PhotoImage(file='img2.png'),
        tk.PhotoImage(file='img3.png')
]
msgs=[
        '体を冷やさないようにしましょう。',
        '過ごしやすい日です。',
        'こまめに水分補給をしｋてください。',
        '危険な暑さです。注意してください。'
]

def draw_txt(txt,x,y,size,color,tag):
    fnt=('Arial',size,'bold')
    cvs.create_text(x+1,y+1,text=txt,fill='#333',font=fnt,tag=tag)
    cvs.create_text(x,y,text=txt,fill=color,font=fnt,tag=tag)

def btn_click():
    temp=int(e1.get())
    fumi=int(e2.get())
    result=(0.81*temp)+(0.01*fumi)*((0.99*temp)-14.3)+46.3

    if result<60:
        index=0
    elif result<70:
        index=1
    elif result<80:
        index=2
    else:
        index=3
    cvs.delete('BG')
    cvs.create_image(200,200,image=images[index],tag='BG')
    cvs.delete('TXT')
    draw_txt(f'気温は{temp}度、湿度は{fumi}%',200,30,22,f_colors[index],'TXT')
    draw_txt(f'不快指数は{result:.1f}',200,80,22,f_colors[index],'TXT')
    draw_txt(msgs[index],200,130,18,f_colors[index],'TXT')

fnt=('Arial',18)
s1={'padx':15,'pady':(20,5),'anchor':tk.W}
s2={'padx':15,'pady':(5,5),'anchor':tk.W}
tk.Label(text='温度(c)',bg='skyblue',font=fnt).pack(**s1)
e1=tk.Entry(width=10)
e1.pack(**s2)
tk.Label(text='湿度(%)',bg='skyblue',font=fnt).pack(**s2)
e2=tk.Entry(width=10)
e2.pack(**s2)
btn=tk.Button(text='計算する',font=fnt,command=btn_click).pack(**s1)
cvs=tk.Canvas(width=400,height=400,bg='skyblue',bd=0,highlightthickness=0,relief='ridge')
cvs.pack(pady=20)
root.mainloop()
