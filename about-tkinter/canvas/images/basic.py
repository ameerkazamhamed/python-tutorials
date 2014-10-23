import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=85, height=105)
canvas.pack()
image = tk.PhotoImage(file='./image.gif')
canvas.create_image(0,0,image=image,anchor=tk.NW)
canvas.bind_all('<Button-1>',lambda e: exit())
root.mainloop()

