import tkinter as tk
import tkinter.ttk as ttk

class Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen = Screen().pack()

    def run(self):
        return self.mainloop()

class Screen(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spritesheet = tk.PhotoImage(file="avatar.gif")
        self.imgnum = 179
        self.imglast = 0
        self.images = [self.subimage(70*i, 0, 70*(i+1), 50) for i in range(self.imgnum)]
        self.room = tk.Canvas(self, width=70, height=60)
        self.room.pack()
        self.room.bind_all('<Button-1>',lambda e: exit())
        self.draw(0)

    def subimage(self, l, t, r, b):
        image = tk.PhotoImage()
        image.tk.call(image, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return image

    def draw(self, sprite):
        self.room.delete(self.imglast)
        self.imglast = self.room.create_image(35, 30, image=self.images[sprite])
        self.after(5, self.draw, (sprite+1) % self.imgnum)

if __name__ == '__main__':
    Game().run()
