from tkinter import Tk,Button

def action_print():
    print('Hello World')

def action_exit():
    print('Ok, goodbye.')
    exit()

window = Tk()
window.wm_title('Hello GUI World')
button1 = Button(window, text="Don't Press Me", command=action_print)
button2 = Button(window, text="Had Enough?", command=action_exit)
button1.pack()
button2.pack()

input()
