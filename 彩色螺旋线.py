import turtle

screen = turtle.Screen()
screen.setup(600,400)
screen.bgcolor("lightblue")
screen.title("我的个性化名片")

pen = turtle.Turtle()
pen.speed(3)
pen.hideturtle()

def draw_card():
    pen.penup()
    pen.goto(-200,150)
    pen.pendown()

    pen.color("darkblue","white")
    pen.begin_fill()

    for i in range(2):
        pen.forward(400)
        pen.right(90)
        pen.forward(300)
        pen.right(90)

    pen.end_fill()

def draw_decorations():
    pen.penup()
    pen.goto(-180,120)
    pen.pendown()
    pen.color("orange")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill


    pen.penup()
    pen.goto(150,-120)
    pen.down()
    pen.color("pink")
    for i in range(6):
        pen.forward(20)
        pen.backward(20)
        pen.right(60)

        
def write_text():
    pen.penup()

    pen.goto(-180,100)
    pen.color("black")
    pen.write("张三",font=("楷体",24,"bold"))

    pen.goto(-180,70)
    pen.color("darkblue")
    pen.write("南昌大学 人工智能实验251班",font=("宋体",14,"normal"))

    pen.goto(-180,50)
    pen.pendown()
    pen.pensize(1)
    pen.forward(360)
    pen.penup()
              
    pen.goto(-180,20)
    pen.write("电话：15575659608",font=("宋体",12,"normal"))
              
    pen.goto(-180, -10)
    pen.write("邮箱: zhangsan@email.com", font=("宋体", 12, "normal"))             
 
    pen.goto(-180, -50)
    pen.write("热爱编程的计算机学生", font=("宋体", 12, "normal"))
    
    pen.goto(-180, -80)
    pen.write("喜欢Python和算法设计", font=("宋体", 12, "normal"))
    

    pen.goto(100, -120)
    pen.color("gray")
    pen.write("—— 期待交流 ——", font=("楷体", 10, "italic"))
    
draw_card()
draw_decorations()
write_text()

pen.goto(0,180)              
pen.color("darkgreen")
pen.write("点击屏幕退出")

screen.exitionclick()
              
print("名片绘制完成")





















    
