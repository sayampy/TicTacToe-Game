#import curses as curs
from .random_move import random_move
from .human_move import human_move
from inspect import signature as sign

modes = {
    'human':human_move,
    'random':random_move,
}
# Variable Name stand for
# stdscr: win
# cell_num: tictactoe cell number between 1-9
# cell_win: subwindow of cell_num
# points: dict of which cells are empty
# moves: dict of game moves

class Mode():
    def __init__(self, window, mode_name):
        self.mode_name = mode_name
        self.move_func = modes.get(self.mode_name)
        self.win = window
    def __repr__(self):
        return f'tictactoe.move_modes.Mode(mode_name={self.mode_name})'
    def make_move(self,**kwargs):
        func_args = list(sign(self.move_func).parameters)
        func_kwargs = {key:value for key,value in kwargs.items() if key in func_args}
        cell_num = self.move_func(**func_kwargs) ## move~func must be return cell_num
        if cell_num in (False,None):
            return
        return self.place_move(kwargs['player'],cell_num,
                kwargs['points'])
    def place_move(self,player,cell_num,points):
        cell_win = points[cell_num]
        __count=len(player.split('\n'))
        for text in player.split('\n'):
            cell_win_y, cell_win_x = cell_win.getmaxyx()
            cell_win.addstr(
                (cell_win_y - __count)//2,
                (cell_win_x - len(text))//2,
                text)
            __count=-1
        cell_win.refresh()
        points.pop(cell_num)
        return points,cell_num

