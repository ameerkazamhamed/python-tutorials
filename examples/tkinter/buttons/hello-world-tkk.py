'''
This is 'hello world' in modern tkinter/ttk style.

Don't worry if that doesn't make any sense, just know it is the most
modern, accessible, and available way to make cool graphics apps in
Python.

For those that are familiar with tkinter we use `import tkinter as tk`
as a standard (as opposed to what some call the "standard" alternative
`from tkinter import *`) because it is the most explicit and makes the
most sense to both those that are new to tkinter programming as well
as those that have been doing it for decades. This is the same reason
for `import tkinter.ttk as ttk` instead of the `from` alternative. The
explicit prefixes ensure -- in Pythonic style -- there is never a question
about which type of widget you are using and that's important because
using the ttk widgets requires a different syntax for styling.
'''

import tkinter as tk
import tkinter.ttk as ttk

def do_print():
    print('Hello World')

def do_exit():
    print('Ok, goodbye.')
    exit()

# use a root controller with a child frame since the root 
# controller itself is not themable but the child is
root = tk.Tk()
main = ttk.Frame(root).pack()

root.wm_title('Hello GUI World')
button1 = ttk.Button(main, text="Don't Press Me", command=do_print).pack()
button2 = ttk.Button(main, text="Had Enough?", command=do_exit).pack()
root.mainloop()
