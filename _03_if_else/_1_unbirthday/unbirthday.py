import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday=simpledialog.askstring(title='Birthday', prompt='When is your birthday?')
    if birthday == 'April 4':
        messagebox.showinfo(title='Happy Birthday', message='Happy Birthday!')
    else:
        messagebox.showinfo(title='Happy Unbirthday', message='Happy Unbirthday!')