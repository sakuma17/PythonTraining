import random
import turtle
ts=[]

def setup():
    global ts
    startline=-620
    screen=turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic('pavement.gif')

    t_y=[-40,-20,0,20,40]
    t_color=['blue','cyan','magenta','pink','green']

    for i in range(len(t_y)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.color(t_color[i])
        t.penup()
        t.setpos(startline,t_y[i])
        #t.pendown()
        ts.append(t)

def race():
    global ts
    finishline=540
    t_speed=[[0,10],[0,10],[0,10],[0,10],[2,12]]

    while True:
        for current_t in ts:
            move=random.randint(t_speed[i][0],t_speed[i][1])
            current_t.forward(move)

            x=current_t.xcor()
            if x >=finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'normal'))
                break
        else:
            continue
        break

setup()
race()
turtle.mainloop()
