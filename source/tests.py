import numpy as np
from amateur_2048 import TheGame


def top_down():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]])
    a.move_down()
    b = np.array([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [2, 2, 2, 2]])
    test = a.game_matrix == b
    assert (False not in test)


def down_top():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [2, 2, 2, 2]])
    a.move_up()
    b = np.array([[2, 2, 2, 2],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def right_left():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[0, 0, 0, 2],
                              [0, 0, 0, 2],
                              [0, 0, 0, 2],
                              [0, 0, 0, 2]])
    a.move_left()
    b = np.array([[2, 0, 0, 0],
                  [2, 0, 0, 0],
                  [2, 0, 0, 0],
                  [2, 0, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def left_right():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 0, 0, 0],
                              [2, 0, 0, 0],
                              [2, 0, 0, 0],
                              [2, 0, 0, 0]])
    a.move_right()
    b = np.array([[0, 0, 0, 2],
                  [0, 0, 0, 2],
                  [0, 0, 0, 2],
                  [0, 0, 0, 2]])
    test = a.game_matrix == b
    assert (False not in test)


def add_down():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2]])
    a.move_down()
    b = np.array([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [4, 4, 4, 4],
                  [4, 4, 4, 4]])
    test = a.game_matrix == b
    assert (False not in test)


def add_up():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2]])
    a.move_up()
    b = np.array([[4, 4, 4, 4],
                  [4, 4, 4, 4],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def add_left():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2]])
    a.move_left()
    b = np.array([[4, 4, 0, 0],
                  [4, 4, 0, 0],
                  [4, 4, 0, 0],
                  [4, 4, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def add_right():
    a = TheGame()
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2],
                              [2, 2, 2, 2]])
    a.move_right()
    b = np.array([[0, 0, 4, 4],
                  [0, 0, 4, 4],
                  [0, 0, 4, 4],
                  [0, 0, 4, 4]])
    test = a.game_matrix == b
    assert (False not in test)


def test_win():
    a = TheGame()
    a.testing_mode = True
    a.verbose = False
    a.initialize_start_matrix()
    a.game_matrix = np.array([[0, 0, 0, 0],
                              [0, 1024, 0, 0],
                              [0, 1024, 0, 0],
                              [0, 0, 0, 0]])
    a.move_down()
    assert (a.win is True)


def test_lose():
    a = TheGame()
    a.verbose = False
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 4, 2, 4],
                              [4, 2, 4, 2],
                              [2, 4, 2, 4],
                              [4, 2, 4, 2]])
    a.move_down()
    assert (a.over is True)


def test_move_still_possible():
    a = TheGame()
    a.verbose = False
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 2, 2],
                              [4, 4, 0, 4],
                              [2, 2, 2, 2],
                              [4, 4, 4, 4]])
    assert (a.over is False)


def test_addition():
    a = TheGame()
    a.verbose = False
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[2, 2, 4, 4],
                              [8, 8, 16, 16],
                              [32, 32, 64, 64],
                              [128, 128, 256, 256]])
    a.move_left()
    b = np.array([[4, 8, 0, 0],
                  [16, 32, 0, 0],
                  [64, 128, 0, 0],
                  [256, 512, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def test_addition2():
    a = TheGame()
    a.verbose = False
    a.testing_mode = True
    a.initialize_start_matrix()
    a.game_matrix = np.array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 2, 2, 2],
                              [0, 0, 0, 0]])
    a.move_left()
    b = np.array([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [4, 2, 0, 0],
                  [0, 0, 0, 0]])
    test = a.game_matrix == b
    assert (False not in test)


def run_all():
    tests = [top_down, down_top, left_right, right_left, add_down, add_up, add_left, add_right,
             test_lose, test_move_still_possible, test_addition, test_addition2]
    cnt = 0
    for test in tests:
        try:
            print(test.__name__)
            test()
            print(' PASSED')
            cnt += 1
        except:
            print(' FAILED')
    if cnt == len(tests):
        print('\nALL TESTS PASSED')
    else:
        print('\nSOME TESTS FAILED')


run_all()
