import curses as curs
from curses import *
from collections import namedtuple
def human_move(win,points,recent_player):
    curs.KEY_EXIT = ord('q')
    key = win.getch()
    match key:
        case curs.KEY_EXIT:
            exit()
        case curs.KEY_RESIZE:
            win.redrawwin()
        case key if key in list(map(ord, map(str, range(1,10))) ):
            cell_num = int(chr(key))
            if points.get(cell_num)!=None: cell_win = points[cell_num]
            else: curs.beep();return False # no move
            __count=len(recent_player.split('\n'))
            for text in recent_player.split('\n'):
                cell_win_y, cell_win_x = cell_win.getmaxyx()
                cell_win.addstr(
                    (cell_win_y - __count)//2,
                    (cell_win_x - len(text))//2,
                    text)
                __count=-1
            cell_win.refresh()
            points.pop(cell_num)
            return points,cell_num
