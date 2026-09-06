import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(150):
    t.pencolor(colors[i % 6])
    t.width(2)
    t.forward(i*2)
    t.left(59)
turtle.done()
