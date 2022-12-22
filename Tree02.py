import turtle as t  
from turtle import *
import random as r
import time

n = 100.0

speed("fastest") 
screensize(bg='black')  
left(90)
forward(3 * n)
color("orange", "yellow")  
begin_fill()
left(126)

for i in range(5):  
    forward(n / 5)
    right(144)  
    forward(n / 5)
    left(72)  
end_fill()
right(126)


def drawlight():  
    if r.randint(0, 30) == 0:  
        color('tomato')  
        circle(6)  
    elif r.randint(0, 30) == 1:
        color('orange')  
        circle(3)  
    else:
        color('dark green')  


color("dark green")  
backward(n * 4.8)


def tree(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

for i in range(200):  
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red") 
t.write("Merry Christmas ", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小


def drawsnow():  
    t.ht() 
    t.pensize(2) 
    for i in range(200): 
        t.pencolor("white")  
        t.pu() 
        t.setx(r.randint(-350, 350))  
        t.sety(r.randint(-100, 350)) 
        t.pd()  
        dens = 6  
        snowsize = r.randint(1, 10) 
        for j in range(dens): 
           
            t.fd(int(snowsize))
            t.backward(int(snowsize))
           
            t.right(int(360 / dens))  


drawsnow()  
t.done()  


