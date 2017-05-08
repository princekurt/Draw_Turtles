import turtle


def main():
    # Initialize the screen
    window = turtle.Screen()
    window.bgcolor("white")

    # Initialize the cursor
    cursor = turtle.Turtle()
    cursor.shape("turtle")
    cursor.color("blue")
    cursor.speed(100)

    # Draw a circle of the requested Shape
    for i in range (0,45):
        draw_triangle(cursor)
        cursor.right(8)
    window.exitonclick()
    
def draw_square(mTurtle):
    # Draws a Square
    for x in range (0,4):
        mTurtle.forward(100)
        mTurtle.right(90)
        

def draw_triangle(mTurtle):
    # Draws a triangle
    for x in range (0,3):
        mTurtle.forward(100)
        mTurtle.right(120)

main()

