print ('hello world')
print("hello GOA my name is giorgi")
 
from turtle import *
#we want to paint a hous 
width(5)
color("orange")
speed(20)
#step 1 draw a square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
left(90)
forward(120)    #height of door 
begin_fill()
right(90)       
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
color("brown")
begin_fill()
left(30)
forward(20)
left(90)
forward(15)
pendown()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

exitonclick()