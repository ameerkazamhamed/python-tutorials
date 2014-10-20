tkinter/tkk
===========

Bunch of snippets illustrating different components of the standard
[tkinter](https://docs.python.org/3.4/library/tkinter.html) and the
standard [tkk](https://docs.python.org/3.4/library/tkinter.ttk.html)
extension.

**Always use the `tkk` versions of components when they are available.**

Despite the use elsewhere of `from tkinter import *` and
`from tkinter import ttk` which many document as 'standard'
idioms the samples in this repo follow an arguably [more Pythonic
approach](https://docs.python.org/3.4/howto/doanddont.html), which is
easier for most beginners to follow and debug:

```python
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
main = ttk.Frame(root)
```
This has the added advantage of automatically getting around the fact
that the root Tk component cannot itself be styled, only subcomponents.

Also see the [revised Bubble Blaster
project](https://github.com/skilstak/dk-help-your-kids-with-computer-coding/blob/master/bubble-blaster/revised-oop.py)
for one way to incorporate tkinter/tkk into your object-oriented games
and other projects.

Documentation Resources
=======================

Unless otherwise noted following materials are freely available online,
in PDF or otherwise:

### [Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)

http://www.tutorialspoint.com/python/python_gui_programming.htm

