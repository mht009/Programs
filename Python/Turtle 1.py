import turtle

star = turtle.Turtle()

s = turtle.Screen()
s.bgcolor("black")

star.width(2)
star.speed(0)

col = ("white", "blue", "green", "yellow", "cyan", "red")

for i in range(8):
    star.forward(80)
    star.right(144)
    star.color(col[i%4])

    for b in range(6):
        star.forward(80)
        star.left(144)

        for k in range(6):
            star.forward(80)
            star.right(144)

turtle.mainloop()
