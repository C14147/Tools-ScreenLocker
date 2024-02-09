Attention: The author of this repository is Chinese and his English is not very well.

## Description

This is only a Python file. The program will close your `explorer.exe` and use tkinter to create a top-most GUI let you can't use your computer.

## Command Line Args

```
usage: screenlocker.exe [-h] [-s second] [-bg colour] [-fg colour] [-font Font] [-lang lang]

Lock Your PC when the countdown done.

optional arguments:
  -h, --help  show this help message and exit
  -s second   Lock screen's time(s)
  -bg colour  Screen's Background Colour
  -fg colour  Screen's Text Colour
  -font Font  Screen's Text's Font Style
  -lang lang  App's Language(0:en, 1:cn)
```

## Online Help

I try to use ctype.user32 to Disable Keyboard & Mouse.

```python
from ctypes import *

user32 = windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
user32.BlockInput(True)
```

I run the progam. It disable my keyboard and mouse, but the program can't countdown and exit. Where is the problem?
