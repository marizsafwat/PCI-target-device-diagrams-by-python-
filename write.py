import math
import random
import turtle
import time

#write operation

#pointers
pointers = turtle.Turtle()
pointers.penup()
pointers.setposition(-150,230)
pointers.pendown()
pointers.color('black')

t=0
while(t<9):
    pointers.right(90)
    pointers.forward(530)
    pointers.penup()
    pointers.left(90)
    pointers.forward(50)
    pointers.left(90)
    pointers.forward(530)
    pointers.right(90)
    pointers.pendown()
    t=t+1

pointers.speed(1)
pointers.hideturtle()


#reset signal
reset = turtle.Turtle()
reset.penup()
reset.setposition(-200,210)
reset.pendown()
reset.write('Reset', align='left')

reset.pensize(3)
reset.color('blue')
reset.forward(50)
reset.left(90)
reset.forward(50)
reset.right(90)
reset.forward(50)
reset.right(90)
reset.forward(50)
reset.left(90)
reset.forward(350)
reset.speed(2)


# clk signal
clk = turtle.Turtle()

clk.penup()
clk.setposition(-200,135)
clk.pendown()
clk.color('red')
clk.pensize(3)
clk.write('Clock', align='left')

i = 0
while(i<4):
    clk.forward(50)
    clk.left(90)
    clk.forward(50)
    clk.right(90)
    clk.forward(50)
    clk.right(90)
    clk.forward(50)
    clk.left(90)
    i=i+1
clk.forward(50)
clk.speed(2)

#frame
frame = turtle.Turtle()
frame.color('green')
frame.pensize(3)

frame.penup()
frame.setposition(-200,110)
frame.pendown()
frame.write('Frame', align='left')

frame.forward(100)
frame.right(90)
frame.forward(50)
frame.left(90)
frame.forward(200)
frame.left(90)
frame.forward(50)
frame.right(90)
frame.forward(150)

frame.speed(2)


#address
address = turtle.Turtle()
address.penup()
address.setposition(-200,10)
address.pendown()
address.color('dark blue')
address.pensize(3)
address.write('AD', align='left')

address.forward(100)
k=0

#shape
while (k <3):
    address.begin_fill()
    address.left(90)
    address.forward(25)
    address.right(90)
    address.forward(100)
    address.right(90)
    address.forward(50)
    address.right(90)
    address.forward(100)
    address.right(90)
    address.forward(25)
    address.penup()
    address.right(90)
    address.forward(100)
    address.pendown()
    if k==0:
        address.end_fill()
    k=k+1
address.forward(50)
address.speed(2)


#control
control = turtle.Turtle()
control.penup()
control.setposition(-200,-70)
control.pendown()
control.color('yellow')
control.pensize(3)
control.write('CBE', align='left')


control.forward(100)
h=0

#shape
while (h <3):
    control.begin_fill()
    control.left(90)
    control.forward(25)
    control.right(90)
    control.forward(100)
    control.right(90)
    control.forward(50)
    control.right(90)
    control.forward(100)
    control.right(90)
    control.forward(25)
    control.penup()
    control.right(90)
    control.forward(100)
    control.pendown()
    if h==0:
        control.end_fill()
    h=h+1
control.forward(50)
control.speed(2)


#irdy  signal
irdy=turtle.Turtle()
irdy.penup()
irdy.setposition(-200,-115)
irdy.pendown()
irdy.color('purple')
irdy.pensize(3)
irdy.write('IRDY', align='left')

irdy.forward(200)
irdy.right(90)
irdy.forward(50)
irdy.left(90)
irdy.forward(200)
irdy.left(90)
irdy.forward(50)
irdy.right(90)
irdy.forward(50)

irdy.speed(2)

#trdy signal
trdy=turtle.Turtle()
trdy.penup()
trdy.setposition(-200,-185)
trdy.pendown()
trdy.color('orange')
trdy.pensize(3)
trdy.write('TRDY', align='left')

trdy.forward(200)
trdy.right(90)
trdy.forward(50)
trdy.left(90)
trdy.forward(200)
trdy.left(90)
trdy.forward(50)
trdy.right(90)
trdy.forward(50)

trdy.speed(2)


#devsel signal
dev=turtle.Turtle()
dev.penup()
dev.setposition(-200,-255)
dev.pendown()
dev.color('grey')
dev.pensize(3)
dev.write('DEVSEL', align='left')

dev.forward(200)
dev.right(90)
dev.forward(50)
dev.left(90)
dev.forward(200)
dev.left(90)
dev.forward(50)
dev.right(90)
dev.forward(50)

dev.speed(2)

turtle.done()