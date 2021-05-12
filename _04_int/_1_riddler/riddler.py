"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    riddle1 = simpledialog.askstring(title='Riddle 1', prompt='How do spiders communicate?')
    riddlecount = 0
    if riddle1 == 'The worldwide web':
        riddlecount += 1
    else:
        riddlecount += 0
    riddle2 = simpledialog.askstring(title='Riddle 2', prompt='The more you take, the more you leave behind. What am I?')
    if riddle2 == 'Footsteps':
        riddlecount += 1
    else:
        riddlecount += 0
    riddle3 = simpledialog.askstring(title='Riddle 3', prompt='What has a head, a tail, is brown, and has no legs?')
    if riddle3 == 'A penny':
        riddlecount += 1
    else:
        riddlecount += 0
    str(riddlecount)
    messagebox.showinfo(title='Final Score', message='You got ' +str(riddlecount)+ ' riddles correct')