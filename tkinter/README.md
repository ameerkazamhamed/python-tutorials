tkinter/ttk
===========

Bunch of snippets illustrating different components of the standard
[tkinter](https://docs.python.org/3.4/library/tkinter.html) and the
standard [ttk](https://docs.python.org/3.4/library/tkinter.ttk.html)
extension.

**Always use the `ttk` versions of components when they are available.**

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
for one way to incorporate tkinter/ttk into your object-oriented games
and other projects.

Documentation Resources
=======================

Unless otherwise noted following materials are freely available online,
in PDF or otherwise:

#### [DK Help Your Kids with Computer Coding](https://github.com/skilstak/dk-help-your-kids-with-computer-coding)

Link is to SkilStak's GitHub site documenting and extending it.

This inexpensive book is one of SkilStak's standard recommendations
for its approachability and great style despite some of its errors and
less-than-desirable technology choices and descriptions.

Only `tkinter.colorpicker` and `tkinter.Canvas` are used, but this is
fine since these are the most fun for beginners.

Be warned that the Bubble Blaster project in
particular needs reworking, which we have
[revised](https://github.com/skilstak/dk-help-your-kids-with-computer-coding/bubble-blaster).

#### [Modern Tkinter for Busy Python Developers](http://www.amazon.com/Modern-Tkinter-Busy-Python-Developers-ebook/dp/B0071QDNLO)

Heavily focuses on the main widgets and not as much on `tkinter.Canvas`
but points out the importance of using `ttk` (modern `tkinter`) and
how. Can be purchased for Kindle on Amazon and probably worth the $10
or so.

#### [Python interface to Tcl/Tk](https://docs.python.org/3.4/library/tkinter.html)

The standard Python `tkinter` 3.4 documentation.

#### [Tk themed widgets](https://docs.python.org/3.4/library/tkinter.ttk.html)

The standard Python `ttk` 3.4 documentation.

## Dated

These continue to show up in searches and while they have a lot of useful
information &mdash; especially for pre-`ttk` (8.5) components such as
`tkinter.Canvas` &mdash; they are really out of date, some by as much
as 10 years.

#### [An Introduction to Tkinter](http://effbot.org/tkinterbook/)

Still labeled a 'Work in Progress' after the last update was on November
2005, but still has helpful stuff &mdash; especially for `tkinter.Canvas`
and the other components not affected by the 8.5 `ttk` update.

#### [Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)

Pretty dated information, including the `from Tkinter import *` and `from
ttk import *` references, but the discussion of the different components and
parameters to them seems good.

#### [Python GUI Programming](http://www.tutorialspoint.com/python/python_gui_programming.htm)

Definitely dated information (using the old `Tkinter` reference instead of
`tkinter`) but useful &mdash; especially for pre-`ttk` components.

