Images
======

The only image format supported by by `tkinter` worth mentioning is
GIF. You can either load them from files or embed them in your programs by
encoding them in binhex and then setting variables with the binhex data.
Which method you use depends on when you want to incur the load time,
which almost never would be detectable for small images for games and
such. Putting them all into binhex will load the fastest because it
is only one file that has to be opened instead of several, but if you
put all your images into a sprite sheet, which you probably should do,
then you are only opening a single file anyway.

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
