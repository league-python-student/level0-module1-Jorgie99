import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    enter=simpledialog.askstring(title='Names', prompt='Enter a name')

    if enter == 'Will':
        messagebox.showinfo(title='Will', message='Will is learning ASL')
    if enter == 'Ella':
        messagebox.showinfo(title='Ella', message='Ella is learning Mandarin')
    if enter == 'Erik':
        messagebox.showinfo(title='Erik', message='Erik took Latin')