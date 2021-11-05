import curses as curs
import random
from time import sleep
def random_move(points, player):
    if points == dict():
        # if no cells are empty
        return False
    
    cell_num = random.choice(list(points.keys()))
    '''cell_win = points[cell_num]
    __count=len(recent_player.split('\n'))
    for text in recent_player.split('\n'):
        cell_win_y, cell_win_x = cell_win.getmaxyx()
        cell_win.addstr(
            (cell_win_y - __count)//2,
            (cell_win_x - len(text))//2,
            text)
        __count=-1
    cell_win.refresh()
    points.pop(cell_num)'''
    return player, cell_num
