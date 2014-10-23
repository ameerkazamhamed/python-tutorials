import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
canvas = tk.Canvas(root, width=60, height=70)
canvas.pack()
triangle = canvas.create_polygon(10,10,10,60,50,35,fill='',outline='black')
canvas.move(triangle,5,0)
canvas.tag_bind(triangle,'<Button-3>',lambda e: print(e.__dict__))
canvas.bind_all('<Button-1>',lambda e: exit())
root.mainloop()
