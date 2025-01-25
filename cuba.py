import turtle

# Bandeira de Cuba
# Feito por Caio Wesley, Pedro Lucas e Yuri Teixeira

t = turtle.Turtle()
t.speed(10) 

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
  t.forward(100)
  t.left(90)
  t.forward(65)
  t.left(90)
t.end_fill()

t.up()
t.left(90)
t.forward(13)
t.down()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
  t.forward(13)
  t.right(90)
  t.forward(100)
  t.right(90)
t.end_fill()

t.up()
t.forward(26)
t.right(90)
t.down()

t.fillcolor("white")
t.begin_fill()
for i in range(2):
  t.forward(100)
  t.left(90)
  t.forward(13)
  t.left(90)
t.end_fill()

t.left(90)
t.up()
t.forward(26)
t.right(125)
t.down()

t.fillcolor("red")
t.begin_fill()
for i in range(2):
  t.forward(57)
  t.right(110)
t.right(15)
t.forward(65)
t.end_fill()

t.up()
t.back(29)
t.right(90)
t.forward(7)
t.down()

t.fillcolor("white")
t.begin_fill()
for i in range(5):
  t.forward(19)
  t.right(144)
t.end_fill()
t.up()
t.forward(200)
