Images
======

The only image format supported by by `tkinter` worth mentioning is
GIF. You can either load them from files or embed them in your programs
by encoding them in binhex and then setting variables with the binhex
data, but don't do that. Just create separate files or a single sprite
sheet depending on how many you have.

Both methods are show here.

Other Image Formats
===================

The Python Image Library only works with 2.7 currently. Pillow, it's
'friendly' 3.x fork looks like the future but is still a `pip install`.
While you can certainly incorporate Pillow into your `tkinter/ttk`
projects you should consider waiting and doing that after moving on a
more serious GUI framework (Kivy, Pygame, SDL2, etc.) Remember the point
here is to use the resources available in the standard Python install
as much as possible.

away.
