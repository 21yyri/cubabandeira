import turtle
import time

# Bandeira de Cuba
# INTRODUÇÃO A PROGRAMAÇÂO, INFO1M
# Feito por Caio Wesley, Pedro Lucas e Yuri Teixeira

t = turtle.Turtle()
t.speed(10) 

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
  t.forward(300)
  t.left(90)
  t.forward(195)
  t.left(90)
t.end_fill()

t.up()
t.left(90)
t.forward(39)
t.down()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
  t.forward(39)
  t.right(90)
  t.forward(300)
  t.right(90)
t.end_fill()

t.up()
t.forward(78)
t.right(90)
t.down()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
  t.forward(300)
  t.left(90)
  t.forward(39)
  t.left(90)
t.end_fill()

t.left(90)
t.up()
t.forward(78)
t.right(125)
t.down()

t.fillcolor("red")
t.begin_fill()
for i in range(2):
  t.forward(171)
  t.right(110)
t.right(15)
t.forward(195)
t.end_fill()

t.up()
t.back(87)
t.right(90)
t.forward(21)
t.down()

t.fillcolor("white")
t.color("white")
t.begin_fill()
for i in range(5):
  t.forward(57)
  t.right(144)
t.end_fill()

t.up()
t.forward(20)
t.down()

t.speed(3)
t.fillcolor('white')
t.begin_fill()
for _ in range(5):
  t.forward(14)
  t.right(70)
t.end_fill()

turtle.mainloop()
