import turtle

def draw_square():
    
    window = turtle.Screen()
    window.bgcolor("white")
    
    cursor = turtle.Turtle()
    cursor.shape("turtle")
    cursor.color("blue")
    
    cursor.forward(100)
    cursor.right(90)
    cursor.forward(100)
    cursor.right(90)
    cursor.forward(100)
    cursor.right(90)
    cursor.forward(100)
    cursor.right(90)
    

    window.exitonclick()


draw_square()
