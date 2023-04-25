
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(4)
t.speed(30)
col = ("teal", "yellow", "magenta")
for i in range(200):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(120)