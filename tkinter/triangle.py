from tkinter import Tk,Canvas

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
triangle = canvas.create_polygon(10,10,10,60,50,35)
canvas.move(triangle,5,0)

input()
