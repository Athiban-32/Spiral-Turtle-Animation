from  turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(120):
    color('cyan')
    circle(i)
    color('green')
    circle(i*0.8)
    right(4)
    forward(4)
done()    