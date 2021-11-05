#import curses as curs
from .random_move import random_move
from .human_move import human_move
modes = {
        'human':human_move,
        'random':random_move,
        # new mode must be add here
        }
