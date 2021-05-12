# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius=simpledialog.askinteger(title='Circle Radius', prompt='What is a radius for a circle in pixels?')
    choice=simpledialog.askstring(title='Choice', prompt='Would you like to calculate the area or the circumference?')
    my_turtle=turtle.Turtle()
    my_turtle.circle(radius=radius)
    my_turtle.penup()
    my_turtle.goto(1,1)
if choice == 'area':
    area = math.pi * radius ** 2
    my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 8, 'normal'))
    my_turtle.hideturtle()
    turtle.done()
if choice == 'circumference':
    circumference = 2 * math.pi * radius
    my_turtle.write(arg="circumference = " + str(circumference), move=True, align='left', font=('Arial', 8, 'normal'))
    turtle.done()
#Area = πr^2
#Circumference = 2πr 