import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    password = 'Dare Mighty Things'
    str(password)
    message=simpledialog.askstring(title='Secret', prompt='Type a secret message')
    str(message)
    guess=simpledialog.askstring(title='Guess', prompt='You can only see the secret message if you guess the password')
    if guess == password:
        messagebox.showinfo(title='Secret Message', message=message)
    else:
        messagebox.showerror(title='Error', message='INTRUDER!!')