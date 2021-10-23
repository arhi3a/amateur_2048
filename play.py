from amateur_2048 import TheGame


def play():
    """plays game"""
    game = TheGame()
    game.start()
    while not game.over:
        key = get_key()
        if key == 'w':
            game.move_up()
        elif key == 's':
            game.move_down()
        elif key == 'a':
            game.move_left()
        elif key == 'd':
            game.move_right()
        else:
            print('Unknown key')
        game.print_matrix()


def get_key():
    user = input('wasd')
    return user


play()
