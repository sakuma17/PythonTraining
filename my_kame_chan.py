import turtle
while True:
    num=int(input('亀ちゃんに何角形を描いてもらう?(3以上の半角整数)>>'))
    if(num>=3):
        break
t=turtle.Turtle()
t.shape('turtle')
if num%2==0:
    t.left(90)
else:
    t.right(180)
for _ in range(num):
    t.right(360/num)
    t.forward(100)
turtle.mainloop()
