import turtle
numberofsquare = 5
square = 40
angle = 90
def draw():
     for i in range (2):
        turtle.forward(square * (numberofsquare - 4))
        turtle.left(angle)
     for i in range (2):
       turtle.forward(square * (numberofsquare - 3))
       turtle.left(angle)
     for i in range (2):
         turtle.forward(square * (numberofsquare - 2))
         turtle.left(angle)
     for i in range (2):
         turtle.forward(square * (numberofsquare - 1))
         turtle.left(angle)
     for i in range (3):
        turtle.forward(square * numberofsquare)
        turtle.left(angle)
    
    

draw()
turtle.exitonclick()
