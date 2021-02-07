import turtle
t=turtle.Turtle()
t.shape('turtle')
num=7
for _ in range(num):
    t.forward(100)
    if num%2==0:
        t.right(360/num)
    else:
        t.right(180-(180/num))
turtle.mainloop()
