import curses as curs
from curses import *
from functools import partial
def main(win):
    cell_border=(0,' ',0,0,0,0,0,0)
    ls,rs,ts,bs,tl,tr,bl,br= tuple(cell_border)
    win.border(*cell_border)
    win.refresh()
    win.getkey()

wrapper(main)
