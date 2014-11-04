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
        self.spritesheet = tk.PhotoImage(file="spritesheet.gif")
        self.imgnum = 4
        self.imglast = 0
        self.images = [self.subimage(32*i, 0, 32*(i+1), 48) for i in range(self.imgnum)]
        self.room = tk.Canvas(self, width=32, height=48)
        self.room.pack()
        self.draw(0)

    def subimage(self, l, t, r, b):
        image = tk.PhotoImage()
        image.tk.call(image, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return image

    def draw(self, sprite):
        self.room.delete(self.imglast)
        self.imglast = self.room.create_image(16, 24, image=self.images[sprite])
        self.after(100, self.draw, (sprite+1) % self.imgnum)

if __name__ == '__main__':
    Game().run()
