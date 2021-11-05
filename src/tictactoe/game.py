import curses as curs
from curses import *
import os
from functools import partial
try:
    from . import move_modes
except: import move_modes
from pprint import pprint
__env__={}

DEBUG = False
def debug(*args):
    if DEBUG: 
        endwin()
        pprint(*args)


#LINES = int(os.environ['LINES'])
#COLS = int(os.environ['COLUMNS'])
curs.KEY_EXIT = ord('q')
curs.KEY_NEXT = ord('\n')
'''
def player_move(win,points,recent_player):
    key = win.getch()
    match key:
        case curs.KEY_EXIT:
            return False
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
            return points
'''

def color_combo(num,fore, back):
    #make color pair
    init_pair(num,fore,back)
    return color_pair(num)
def main_win(win, player1,opponent= 'human'): 

    cross = '▀▄▀'+'\n'+'█ █'

    naught = '█▀█'+'\n'+'█▄█'

    start_color()
    win.clear()
    # 
    nocbreak()
    noecho()
    raw()
    nonl()
    #win.nodelay(True)
    win.timeout(0)
    curs_set(0)
    win_y, win_x = win.getmaxyx()
    win.addstr(0,0,'tic tac toe'.center(win_x),
        color_combo(1,COLOR_BLACK,COLOR_WHITE))
    win.refresh()

    player1_move = move_modes.human_move

    player2_move = move_modes.Mode(win,opponent)

    if player2_move == None:
        raise Exception('ModeNotFound','no mode name %s' % opponent)
    cellwin_list = {} # to store 1 to 9 cells/points
    for cell_num in range(1,10):
         cell_win = cell(win, cell_num,win_x,win_y)
         cellwin_list[cell_num]=cell_win
         win.refresh()
    points = cellwin_list.copy()
    #win.doupdate()
    win.keypad(True)

    if player1.lower() in ('x','cross'):
        player1 = cross
        player2 = naught
    elif player1.lower() in ('o','naught'):
        player2 = cross
        player1 = naught
    recent_player = player1
    moves = {}
    def add_move(cell_num,player,moves):
        if player == cross:
            move = 'o'
        else:
            move = 'x'
        moves[cell_num] = move
        return moves
    gameover = False
    while gameover==False:
        if recent_player == player1:
            moved = player1_move(win,points,recent_player)
        elif recent_player == player2:
            moved = player2_move.make_move(points=points,player=recent_player)
        if moved:
            # Player turn switching
            if recent_player == cross:
                recent_player = naught
            else: recent_player = cross ## if player is naught
            points,cell_num = moved
            moves = add_move(cell_num,recent_player,moves)
            gameover = is_gameover(moves)
            debug(moves)
        win.refresh()
    win.attron(A_BOLD)
    if gameover == 'tie':
        win.addstr(2,(win_x-6)//2,'[Tie!]')
    elif gameover[0] in ['X','O']:
        text = gameover[0]+' Win!'
        win.addstr(2,(win_x-len(text))//2, text)
        for cell_num in gameover[1]:
            cell_win = cellwin_list[cell_num]
            cell_win.bkgd(color_combo(2,COLOR_WHITE, COLOR_GREEN))
            cell_win.refresh()
    win.attroff(A_BOLD)
    win.addstr(3,(win_x-len('press enter to continue'))//2,
            'Press ENTER to continue',A_BLINK)
    win.refresh()
    while True:
        match win.getch():
            case curs.KEY_EXIT:
                exit()
            case curs.KEY_NEXT:
                break
        win.refresh()
    endwin()


def cell(win, cell_num,win_x,win_y):
        #make cell
        ##global win_y,win_x
        #y = win_y/4
        #x = win_x/4
        height,width = int(win_y*20/100),int(win_x*20/100)
        x = (win_x-width)/4
        y = (win_y-height)/4
        match cell_num:
            case 1:
                begin_x,begin_y = x,y
                cell_border=[' ',0,' ',0,
                        ' ',' ',' ',0]
            case 2:
                begin_x=x*2
                begin_y = y
                cell_border=[0,0,' ',0,
                        ' ',' ',0,0]
            case 3:
                begin_x=x*3
                begin_y = y
                cell_border=[0,' ',' ',0,
                        ' ',' ',0,' ']
            case 4:
                begin_y = y*2
                begin_x = x
                cell_border=[' ',0,0,0,
                        ' ',0,' ',0]
            case 5:
                begin_y = y*2
                begin_x = x*2
                cell_border=[0,0,0,0,
                        0,0,0,0]
            case 6:
                begin_y = y*2
                begin_x = x*3
                cell_border=[0,' ',0,0,
                        0,' ',0,' ']
            case 7:
                begin_y = y*3
                begin_x = x
                cell_border=[' ',0,0,' ',
                        ' ',0,' ',' ']
            case 8:
                begin_y = y*3
                begin_x = x*2
                cell_border=[0,0,0,' ',
                        0,0,' ',' ']
            case 9:
                begin_y = y*3
                begin_x = x*3
                cell_border=[0,' ',0,' ',
                        0,' ',' ',' ']
            case _:
                begin_x=begin_y=None,None
        try:
            cell_win = win.subwin(height,width,int(begin_y),int(begin_x))
            cell_win.border(*tuple(cell_border))
            cell_win.refresh()
            return cell_win
        except Exception as e:
            endwin()
            print('cell number:',cell_num)
            print('xy:',int(begin_x),int(begin_y))
            print('win:',win_x,win_y)
            print(e)

def center(LINES,COLS,height,width):
    return (
            (LINES-height)//2,
            (COLS-width)//2
            )

from time import sleep
def is_gameover(moves):
    point1_check = list(range(1,4)), [1,4,7], [1,5,9]
    point5_check = list(range(4,7)), [2,5,8], [3,5,7]
    point9_check = list(range(7,10)), [3,6,9]
    for point, _base in zip( [point1_check,point5_check,point9_check], [1,5,9] ):
        for check in point:
            #debug(len(set(list(map( moves.get, check)))))
            set_check = list(map(
                moves.get,
                check
                ))
            debug(set_check)
            '''
            if len(set_check) == 1 and set_check!={None}:
                #sleep(1)
                return 'win',moves.get(_base)
            '''
            if set_check == ['x','x','x']: return 'X',check
            elif set_check == ['o','o','o']: return 'O',check
    if sorted( list(moves.keys()) ) == list(range(1,10)):
        #sleep(1)
        return 'tie'
    else:
        # if game is not over
        return False
if __name__ == '__main__':
    wrapper(partial(main_win, player1 = 'x',opponent='random'))

