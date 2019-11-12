from MaldonadoFunctions import*
turtle.bgcolor("black")

turtle.tracer(False)
for times in range(100):
    swirlparadox(20-times*3)
bob.home()
bob.penup()
bob.forward(50)
bob.pendown()
monster("white")

bob.color("black")
jump(30,100)
bob.circle(5)

jump(-45,100)
bob.circle(5)
turtle.tracer(True)
