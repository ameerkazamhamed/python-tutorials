import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=85, height=105)
canvas.pack()
image = tk.PhotoImage(file='./image.gif')
ref = canvas.create_image(0,0,image=image,anchor=tk.NW)
canvas.update()
canvas.bind_all('<Button-1>',lambda e: exit())

time.sleep(2)
other = tk.PhotoImage(file='./avatar.gif')
canvas.itemconfig(ref,image=other)

root.mainloop()

