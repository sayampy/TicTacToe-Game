import argparse
try: from .tictactoe import game, move_modes
except: from tictactoe import game, move_modes
from functools import partial
parser = argparse.ArgumentParser(prog = 'TicTacToe',
        description = r'''A simple tictactoe game made with curses.
Github: https://github.com/sayampy/TicTacToe-Game''',
        epilog = '''Report issues on https://github.com/sayampy/TicTacToe-Game/issues'''
        )
parser.add_argument('you',help='move for player1 [X/O]',
        nargs = '?',
        const='x')
parser.add_argument('opponent',
        help = 'player2 mode %s' % list(move_modes.modes.keys()),

        )
def main():
    args = parser.parse_args()
    if args.you.lower() in ['x','o']: player1 = args.you.lower()
    else: raise Exception(f'not supported argument {args.you} for player')
    if args.opponent.lower() not in move_modes.modes:
        raise Exception('NoModeFound')
    game.wrapper(partial(
        game.main_win,
        player1=player1,
        opponent=args.opponent.lower()
        ))
if __name__=='__main__':
    main()
