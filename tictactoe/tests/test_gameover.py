def is_gameover(moves):
    point1_check = range(1,4),[1,4,7],[1,5,9]
    point5_check = range(4,7),[2,5,8],[3,5,7]
    point9_check = range(7,10),[3,6,9]
    for point,_base in zip([point1_check,point5_check,point9_check], [1,5,9]):
        for check in point1_check:
            if len(set(map( moves.get,check ))) == 1 and moves.get(_base)!=None:
                return 'win',moves.get(_base)
    return False
