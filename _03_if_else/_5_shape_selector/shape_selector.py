import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.color('black')
    my_turtle.pencolor('black')
    shape = simpledialog.askstring(title='Shapes', prompt='What shape do you want to draw, a triangle, square, or cicle?')
    if shape == 'triangle':
        my_turtle.goto(1, 1)
        my_turtle.begin_fill()
        my_turtle.forward(100)
        my_turtle.left(120)
        my_turtle.forward(100)
        my_turtle.left(120)
        my_turtle.forward(100)
        my_turtle.end_fill()
    if shape == 'square':
        my_turtle.goto(1, 1)
        my_turtle.begin_fill()
        my_turtle.forward(100)
        for i in range(3):
            my_turtle.left(90)
            my_turtle.forward(100)
        my_turtle.end_fill()
    if shape == 'circle':
        my_turtle.penup()
        my_turtle.goto(1, 1)
        my_turtle.begin_fill()
        my_turtle.circle(radius=100)
        my_turtle.end_fill()
    turtle.done()
# Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
