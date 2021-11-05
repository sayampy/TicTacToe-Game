import curses as curs
from curses import *
def main_win(win):
    start_color()
    win.clear()
    nocbreak()
    noecho()

    def color_combo(fore, back):
        #make temporary color pair
        init_pair(1,fore,back)
        return color_pair(1)

    win_y, win_x = win.getmaxyx()
    win.addstr(0,0,'tic tac toe'.center(win_x),
        color_combo(COLOR_BLACK,COLOR_WHITE) )
    board(win)
    win.refresh()
    win.getkey()

def board(win):
    #draw a board
    win_y,win_x = win.getmaxyx()
    def cell(cell_num):
        #make cell
        ##global win_y,win_x
        y,x = win_y//3, win_x//3
        match cell_num:
            case 1:
                cell_border=[' ','│',' ','─',
                        ' ',' ',' ','┘']
            case 2:
                x=x*2
                cell_border=['│','│',' ','─',
                        ' ',' ','└','┘']
            case 3:
                x=x*3
                cell_border=['│',' ',' ','─',
                        ' ',' ','└',' ']
            case 4:
                y = y*2
                cell_border=[' ','│','─','─',
                        ' ','┐',' ','┘']
            case 5:
                y = y*2
                x = x*2
                cell_border=['│','│','─','─',
                        '┌','┐','└','┘']
            case 6:
                y = y*2
                x = x*3
                cell_border=['│',' ','─','─',
                        '┌',' ','└',' ']
            case 7:
                y = y*3
                cell_border=[' ','│','─',' ',
                        ' ','┐',' ',' ']
            case 8:
                y = y*3
                x = x*2
                cell_border=['│','│','─',' ',
                        '┌','┐',' ',' ']
            case 9:
                y = y*3
                x = x*3
        cell_win = win.subwin(5,5,y,x)
        ls,rs,ts,bs,tl,tr,bl,br= tuple(cell_border)
        cell_win.border(ls,rs,ts,bs,tl,tr,bl,br)
    for i in range(1,10):
        cell(i)

wrapper(main_win)
