import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red","purple","blue","green","yellow","orange"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i * 0.5)
    t.left(59)

turtle.done()    
