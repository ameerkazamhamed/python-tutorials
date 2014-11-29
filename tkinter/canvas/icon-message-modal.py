import tkinter as tk
import tkinter.ttk as ttk

class RoundRect():

    def __init__(self,w,x,y,dx,dy,r,f,o):


def round_rect(w,x,y,dx,dy,radius,color='white',tag='round_rect'):
    half = int(radius / 2)
    w.create_oval(x,y,x+radius,y+radius,fill=color,outline=color,tag=tag)
    w.create_oval(dx,dy,dx-radius,dy-radius,fill=color,outline=color,tag=tag)
    w.create_oval(dx-radius,y+radius,dx,y,fill=color,outline=color,tag=tag)
    w.create_oval(x+radius,dy-radius,x,dy,fill=color,outline=color,tag=tag)
    w.create_rectangle(x+half,y,dx-half,dy,fill=color,outline=color,tag=tag)
    w.create_rectangle(x,y+half,dx,dy-half,fill=color,outline=color,tag=tag)


def icon_message(w,x,y,dx,dy,message="",image=None,color='grey',tag='icon_message'):
    radius = 20
    half = int(radius / 2)
    round_rect(w,100,150,300,250,20,'black')
    round_rect(w,100+5,150+5,300-5,250-5,10,'white')
    w.create_image(x+40-50,y,image=image)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
image = tk.PhotoImage(file='image.gif')
icon_message(canvas,150,150,250,200,"Good Job!",image)
canvas.tag_bind('round_rect','<Button-3>',lambda e: print(e.__dict__))
canvas.bind_all('<Button-1>',lambda e: exit())
root.mainloop()
