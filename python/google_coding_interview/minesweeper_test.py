import pytest

import sys
import numpy as np
import random


class Field():
    def __init__(self, rows, cols, num_of_mines):
        self.field = np.array([[0] * cols] * rows)
        self.revealed = np.array([[False] * cols] * rows)

        mine_positions = self.generate_mine_positions(rows, cols, num_of_mines)
        self.locate_mines(self.field, mine_positions)
        
    @staticmethod
    def generate_mine_positions(rows, cols, num_of_mines):
        row_indices = random.sample(range(rows), num_of_mines)
        col_indices = random.sample(range(cols), num_of_mines)

        return list(zip(row_indices, col_indices))

    @staticmethod
    def locate_mines(field, mine_positions):
        adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row, col in mine_positions:
            field[row][col] = 9
            
            for dy, dx in adjacents:
                if 0 < row + dy < field.shape[0] \
                        and 0 < col + dx < field.shape[1] \
                        and field[row + dy][col + dx] != 9:
                    field[row + dy][col + dx] += 1

    def reveal(self, x, y):
        if not (0 < y < self.field.shape[0] and 0 < x < self.field.shape[1]):
            print('OUT OF RANGE')
            return False
        
        self.revealed[y][x] = True
        
        if self.field[y][x] == 9:
            print('BOOM!')
            return False

        if self.field[y][x] == 0:
            adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dy, dx in adjacents:
                if 0 < x + dx < self.field.shape[1] \
                        and 0 < y + dy < self.field.shape[0] \
                        and self.revealed[y + dy][x + dx] == False \
                        and self.field[y + dy][x + dx] == 0:
                    self.reveal(x + dx, y + dy)
        
        return True


    def print(self, print_all=False):
        print('\n')
        for row in range(self.field.shape[0]):
            for col in range(self.field.shape[1]):
                if not print_all \
                        and not self.revealed[row][col]:
                    sys.stdout.write('- ')
                else:
                    sys.stdout.write(str(self.field[row][col]))
                    sys.stdout.write(' ')
            
            print('\n')


def test_generate_mine_positions():
    mine_positions = Field.generate_mine_positions(3, 5, 2)

    assert len(mine_positions) == 2
    assert len(mine_positions[0]) == 2
    assert type(mine_positions[0]) == tuple

def test_create_field():
    field = Field(5, 5, 3)
    field.print()

if __name__ == '__main__':
    field = Field(5, 5, 3)

    x, y = map(int, input().split())

    continue_search = field.reveal(x, y)

    while continue_search:
        field.print()
        x, y = map(int, input().split())
        continue_search = field.reveal(x, y)

    field.print(print_all=True)
