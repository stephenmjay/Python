from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    for dash in range(10):
        pendown()
        forward(10)
        penup()
        forward(5)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
    ada.right(36)
    
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(10):
    bob.right(36)

freida = Turtle()
freida.color('green')
freida.shape('turtle')

freida.penup()
freida.goto(-160, 40)
freida.pendown()

for turn in range(10):
    freida.right(36)

ellie = Turtle()
ellie.color('magenta')
ellie.shape('turtle')

ellie.penup()
ellie.goto(-160, 10)
ellie.pendown()

for turn in range(10):
    ellie.right(36)

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    freida.forward(randint(1, 5))
    ellie.forward(randint(1, 5))
    max = ada.xcor()
    winner = "RED"
    if bob.xcor() > max:
        max = bob.xcor()
        winner = "BLUE"
    if freida.xcor() > max:
        max = freida.xcor()
        winner = "GREEN"
    if ellie.xcor() > max:
        max = ellie.xcor()
        winner = "MAGENTA"

if winner == "RED":
    ada.write("Winner!")
elif winner == "BLUE":
    bob.write("Winner!")
elif winner == "GREEN":
    freida.write("Winner!")
else:
    ellie.write("Winner!")
