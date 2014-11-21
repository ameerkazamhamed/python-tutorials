import tkinter as tk
import tkinter.ttk as ttk

'''
proc roundRect2 {w L T Rad width height colour tag} {
 $w create oval $L $T [expr $L + $Rad] [expr $T + $Rad] -fill $colour -outline $colour -tag $tag
  $w create oval [expr $width-$Rad] $T $width [expr $T + $Rad] -fill $colour -outline $colour -tag $tag
  $w create oval $L [expr $height-$Rad] [expr $L+$Rad] $height -fill $colour -outline $colour -tag $tag
  $w create oval [expr $width-$Rad] [expr $height-$Rad] [expr $width] $height -fill $colour -outline $colour -tag $tag
  $w create rectangle [expr $L + ($Rad/2.0)] $T [expr $width-($Rad/2.0)] $height -fill $colour -outline $colour -tag $tag
  $w create rectangle $L [expr $T + ($Rad/2.0)] $width [expr $height-($Rad/2.0)] -fill $colour -outline $colour -tag $tag
}
'''

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
