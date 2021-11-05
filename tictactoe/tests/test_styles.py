import curses as c
from curses import *
def main(win):
    s = [A_ALTCHARSET, A_CHARTEXT, A_INVIS, A_NORMAL, A_STANDOUT,
            A_ATTRIBUTES, A_COLOR, A_ITALIC, A_PROTECT, A_TOP,
            A_BLINK, A_DIM, A_LEFT, A_REVERSE, A_UNDERLINE,
            A_BOLD, A_HORIZONTAL, A_LOW, A_RIGHT, A_VERTICAL]
    x = 0
    for a in s:
        win.addstr(x,0,str(x),a)
        x+=1
    win.getkey()
    endwin()

wrapper(main)
