import math
import turtle
#太阳设置
sun=turtle.Turtle()
sun.color("yellow")
sun.shape("circle")
def planet(name,color):
	name.pencolor(color)
	name.color(color)
	name.speed(0)
	name.shape("circle")
def orbit(tu,m,n,t):
	a=(m+n)/2
	c=(m-n)/2
	b=pow(pow(a,2)+pow(c,2),0.5)
	x=c+a*math.cos(10*i/t)
	y=b*math.sin(10*i/t)
	tu.goto(x,y)
def begin(m,tu):
        tu.penup()
        tu.goto(m,0)
        tu.pendown()
#行星设置
mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()
planet(mercury,"blue")
planet(venus,"orange")
planet(earth,"grey")
planet(mars,"red")
planet(jupiter,"green")
planet(saturn,"brown")
#行星到达起始位置
begin(69.8,mercury)
begin(107.5,venus)
begin(152.1,earth)
begin(249.2,mars)
begin(326.6,jupiter)
begin(504,saturn)
for i in range(10000000):
	orbit(mercury,69.8,46,88)
	orbit(venus,108.9,107.5,243)
	orbit(earth,152.1,147.1,365.2,)
	orbit(mars,249.2,206.6,687)
	orbit(jupiter,326.6,296.2,1731)
	orbit(saturn,504,451,2708)
