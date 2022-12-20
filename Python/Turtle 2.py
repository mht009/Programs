import turtle

col = ("white", "blue", "green", "yellow", "cyan", "red", "indigo")

screen = turtle.Screen()
#s.bgcolor("black")

turtle.width(2)
turtle.speed(0)



for i in range(10):
    turtle.color(col[i%7])
    turtle.circle(144)
    turtle.right(36)

turtle.screensize(canvwidth = 600, canvheight = 500, bg = "black")
