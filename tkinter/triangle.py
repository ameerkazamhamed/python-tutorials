import tkinter as tk
import tkinter.tkk import ttk

root = tk.Tk()
canvas = tk.Canvas(root, width=60, height=70)
canvas.pack()
triangle = canvas.create_polygon(10,10,10,60,50,35)
canvas.move(triangle,5,0)

input()
