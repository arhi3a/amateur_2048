from pandas import DataFrame
import numpy as np
from random import choice


class TheGame(object):
    """2048 Game"""

    def __init__(self):
        """init"""
        self.game_matrix = None  # game will be stored in here
        self.points = 0  # player points
        self.size = 0  # size of matrix NxN
        self.over = False  # Lose flag
        self.before = None  # for movement comparison
        self.testing_mode = False  # Only for running tests
        self.win = False  # Win flag
        self.verbose = True  # prints matrix after each move
        self.temporary_matrix = None  # Temporary matrix to fix addition issues

    def initialize_start_matrix(self, size: int = 4):
        """initializes empty game matrix
        :param size: size of matrix default 4x4
        only square matrix is possible"""
        self.game_matrix = np.zeros((size, size), dtype=int)
        self.temporary_matrix = np.zeros((size, size), dtype=int)
        self.size = size

    def print_matrix(self):
        """Prints game matrix for visual feedback"""
        if self.verbose is True:
            print(DataFrame(self.game_matrix))

    def create_new_element(self):
        """creates new random element on board
        new possible random values 2,4"""
        values = [2.0, 4.0]
        random_value_to_place = choice(values)
        positions = self.check_possible_to_place()
        if positions is False:  # If no empty places end the game
            self.end_game()
        else:  # place new number on board
            if self.testing_mode is False:
                random_position = choice(positions)
                self.game_matrix[random_position[0]][random_position[1]] = random_value_to_place

    def check_empty(self, row: int, column: int) -> bool:
        """Checks if field in given indexes is empty
        :param row: row
        :param column: column
        :return: True if field is empty, False if field is full"""
        if self.game_matrix[row][column] == 0:
            return True
        else:
            return False

    def check_possible_to_place(self):
        """Checks if there are empty fields to place new number"""
        empty_fields = []
        for row in range(0, self.size):
            for column in range(0, self.size):
                if self.check_empty(row, column):
                    empty_fields.append([row, column])
        if len(empty_fields) == 0:
            return False
        else:
            return empty_fields

    def move_down(self):
        """Moves numbers down"""
        self.check_if_any_move(1)
        self.temporary_matrix = np.zeros((self.size, self.size), dtype=int)
        for row in range(self.size - 2, -1, -1):  # -2 so we don't check bottom row
            for column in range(0, self.size):
                self.movement_logic(1, row, column)
        if self.check_if_any_move(2):
            self.check_if_win()
            self.create_new_element()
        else:
            self.check_if_any_move_possible()

    def move_up(self):
        """Moves numbers up"""
        self.check_if_any_move(1)
        self.temporary_matrix = np.zeros((self.size, self.size), dtype=int)
        for row in range(1, self.size):  # start from 1 so we  don't check top row
            for column in range(0, self.size):  # -1 so we don't get out of index error
                self.movement_logic(2, row, column)
        if self.check_if_any_move(2):
            self.check_if_win()
            self.create_new_element()
        else:
            self.check_if_any_move_possible()

    def move_left(self):
        """Moves numbers left"""
        self.check_if_any_move(1)
        self.temporary_matrix = np.zeros((self.size, self.size), dtype=int)
        for row in range(0, self.size):
            for column in range(1, self.size):  # 1 so we don't check left column
                self.movement_logic(3, row, column)
        if self.check_if_any_move(2):
            self.check_if_win()
            self.create_new_element()
        else:
            self.check_if_any_move_possible()

    def move_right(self):
        """Moves numbers right"""
        self.check_if_any_move(1)
        self.temporary_matrix = np.zeros((self.size, self.size), dtype=int)
        for row in range(0, self.size):
            for column in range(self.size - 2, -1, -1):
                self.movement_logic(4, row, column)
        if self.check_if_any_move(2):
            self.check_if_win()
            self.create_new_element()
        else:
            self.check_if_any_move_possible()

    def check_if_any_move_possible(self):
        """Checks if any move is still possible ex. empty field or possible addition
        :return: True if move possible, False if impossible & marks game over flag"""
        possible_to_place = self.check_possible_to_place()
        if type(possible_to_place) == list:
            return True
        else:
            for row in range(0, self.size):
                for column in range(0, self.size):
                    source = [row, column]
                    # UP
                    target = [row - 1, column]
                    if self.check_if_in_game(target):
                        if self.game_matrix[source[0]][source[1]] == self.game_matrix[target[0]][target[1]]:
                            return True
                    # RIGHT
                    target = [row, column + 1]
                    if self.check_if_in_game(target):
                        if self.game_matrix[source[0]][source[1]] == self.game_matrix[target[0]][target[1]]:
                            return True
            self.end_game()
            return False

    def movement(self, source: list, target: list, row_num: int = 0, column_num: int = 0):
        """
        :param row_num: increase/decrease row number
        :param column_num: increase/decrease column number
        :param source: source row
        :param target: source column
        """
        flag = True
        if self.game_matrix[source[0]][source[1]] != 0:
            while self.check_empty(row=target[0], column=target[1]) and flag is True:
                target[0] += row_num
                target[1] += column_num
                if self.check_if_in_game(target) is False:
                    flag = False
                    target[0] -= row_num
                    target[1] -= column_num
            else:
                if self.game_matrix[target[0]][target[1]] != 0:
                    if self.compare(source, target) and self.temporary_matrix[target[0]][target[1]] != 1:
                        self.addition(source, target)
                    else:
                        target[0] -= row_num
                        target[1] -= column_num
                        if source == target:
                            return None
                        else:
                            self.game_matrix[target[0]][target[1]] = self.game_matrix[source[0]][source[1]]
                            self.game_matrix[source[0]][source[1]] = 0
                else:
                    self.game_matrix[target[0]][target[1]] = self.game_matrix[source[0]][source[1]]
                    self.game_matrix[source[0]][source[1]] = 0

    def movement_logic(self, move_type: int, row: int, column: int):
        """
        :param move_type: 1 - down, 2 - up, 3 - left, 4 - right
        :param row: source row
        :param column: source column
        """
        if move_type == 1:
            source = [row, column]
            target = [row + 1, column]
            self.movement(source, target, 1, 0)

        elif move_type == 2:
            source = [row, column]
            target = [row - 1, column]
            self.movement(source, target, -1, 0)

        elif move_type == 3:
            source = [row, column]
            target = [row, column - 1]
            self.movement(source, target, 0, -1)

        elif move_type == 4:
            source = [row, column]
            target = [row, column + 1]
            self.movement(source, target, 0, 1)

    def check_if_any_move(self, flag: int) -> bool:
        """
        :param flag: flag if it's store or check part 1 - store, 2 - check
        Checks if there are any changes in table if not and no empty fields ends the game
        """
        if flag == 1:
            self.before = np.copy(self.game_matrix)
            return True
        else:
            tmp = self.before == self.game_matrix
            if False not in tmp:
                self.before = None
                return False
        self.before = None
        return True

    def check_if_in_game(self, field: list) -> bool:
        """Checks if field is still withing game
        :param field: list [row, column]
        :return: True if in field, False otherwise"""
        if field[0] > self.size - 1 or field[1] > self.size - 1 or field[0] < 0 or field[1] < 0:
            return False
        else:
            return True

    def addition(self, source: list, target: list):
        """Performs addition of 2 values
        :param source: list of ints with [row,column] of source field
        :param target: list of ints with [row,column] of target field"""
        self.game_matrix[target[0]][target[1]] *= 2  # multiply value by 2
        self.game_matrix[source[0]][source[1]] = 0
        self.temporary_matrix[target[0]][target[1]] = 1
        self.points += self.game_matrix[target[0]][target[1]]  # add points

    def compare(self, source: list, target: list) -> bool:
        """Compares if numbers can be added
        :param source: list of ints with [row,column] of source field
        :param target: list of ints with [row,column] of target field
        :return: bool True if values can be added (values the same), False if not"""
        if self.game_matrix[source[0]][source[1]] == self.game_matrix[target[0]][target[1]]:
            return True
        else:
            return False

    def end_game(self):
        """Ends game"""
        if self.verbose is True:
            print('Game over')
            print('Points:', self.points)
        self.over = True
        return self.points, 'GAME_OVER'

    def check_if_win(self, points: int = 2048):
        """Checks if win condition is meet any field has x points"""
        if points in self.game_matrix:
            self.win = True
            self.end_game()

    def start(self):
        """Starts the game"""
        self.initialize_start_matrix(4)
        self.create_new_element()
        self.print_matrix()
