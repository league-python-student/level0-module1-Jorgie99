"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    number1 = simpledialog.askstring(title='Numbers', prompt='Give me a number')
    number2 = simpledialog.askstring(title='Numbers', prompt='Give me another number')
    option = simpledialog.askstring(title='Numbers', prompt='Do you want to add, subtract, multiply, or divide them?')
    if option == 'add':
        sum = float(number1) + float(number2)
        str(sum)
        messagebox.showinfo(title='Sum', message='The sum is ' +str(sum))
    if option == 'subtract':
        difference = float(number1) - float(number2)
        str(difference)
        messagebox.showinfo(title='Difference', message='The difference is ' + str(difference))
    if option == 'multiply':
        product = float(number1) * float(number2)
        str(product)
        messagebox.showinfo(title='Product', message='The product is ' + str(product))
    if option == 'divide':
        quotient = float(number1) / float(number2)
        str(quotient)
        messagebox.showinfo(title='Quotient', message='The quotient is ' + str(quotient))