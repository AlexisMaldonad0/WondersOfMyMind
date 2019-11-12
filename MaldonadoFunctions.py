import turtle
turtle.colormode(255)
bob=turtle.Turtle()
bob.speed(0)

def design(distance):
    for times in range(100):
        swirlparadox(distance)
        bob.left(120)


def strainedeye(distance):
    for times in range(11):
        bob.begin_fill()
        swirl(distance)
        bob.left(120)
        bob.end_fill()
        
def swirlparadox(distance):
    for times in range(33):
        swirl(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*36)
    
def swirl(distance):
    for times in range(20):
        c=times*12
        bob.color(0,0,0)
        bob.width(times*2)
        bob.forward(distance)
        bob.left(10)

def tile(c):
    polygon(4,200,c)
    for times in range(8):
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(8):
        tile(c)
        bob.forward(200)

def square(distance):
    for times in range(4):
        bob.forward(distance)
        bob.left(90)

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.left(120)

def polygon(sides,distance,c):
    bob.color(c)
    bob.begin_fill()
    sides = 3
    angle = 360 / sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figurel(distance,size,c,):
    bob.color(c)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()

def monster(c):
    bob.color(c)
    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.end_fill()
    
def fadingTriangle():
    for times in range(50):
        c=(250-times*2,250-times*2,0)
        polygon(3,500-times*8,c)
