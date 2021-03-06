import tkinter as tk
import tkinter.ttk as ttk

def round_rect(w,x,y,dx,dy,radius,color='white',tag='round_rect'):
    half = int(radius / 2)
    w.create_oval(x,y,x+radius,y+radius,fill=color,outline=color,tag=tag)
    w.create_oval(dx,dy,dx-radius,dy-radius,fill=color,outline=color,tag=tag)
    w.create_oval(dx-radius,y+radius,dx,y,fill=color,outline=color,tag=tag)
    w.create_oval(x+radius,dy-radius,x,dy,fill=color,outline=color,tag=tag)
    w.create_rectangle(x+half,y,dx-half,dy,fill=color,outline=color,tag=tag)
    w.create_rectangle(x,y+half,dx,dy-half,fill=color,outline=color,tag=tag)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
round_rect(canvas,20,20,380,380,30,'grey')
canvas.tag_bind('round_rect','<Button-3>',lambda e: print(e.__dict__))
canvas.bind_all('<Button-1>',lambda e: exit())
root.mainloop()
