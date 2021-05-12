"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    number1 = simpledialog.askstring(title='Numbers', prompt='Give me a number')
    number2 = simpledialog.askstring(title='Numbers', prompt='Give me another number')
    sum = float(number1) + float(number2)
    str(sum)
    messagebox.showinfo(title='Sum', message='The sum is ' +str(sum))