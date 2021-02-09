import requests as req
import json
import turtle
URL='http://api.open-notify.org/iss-now.json'
screen=None;
iss=None;

#Pythonのインデント修正は範囲選択後に「>」
def setup():
    global iss,screen
    screen=turtle.Screen()
    screen.setup(1000,500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180,-90,180,90)
    iss=turtle.Turtle()
    turtle.register_shape('iss.gif')#画像登録
    iss.shape('iss.gif')#見た目設定
    iss.pencolor('red')
    iss.hideturtle()
    iss.penup()

def track_iss():
    res=req.get(URL)
    data=json.loads(res.text)
    pos=data['iss_position']
    lat=float(pos['latitude'])
    lng=float(pos['longitude'])
    print(f'緯度{lat},経度{lng}')
    iss.goto(lng,lat)
    if not iss.isvisible():
        iss.pendown()
        iss.showturtle()
    canvas=turtle.getcanvas()
    canvas.after(5000,track_iss)

setup()
track_iss()
turtle.mainloop()
