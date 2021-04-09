from random import random
import numpy as np


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [['@' if round(random()) == 0 else '-' for _ in range(self.width)] for _ in range(self.height)]
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def get_visited(self):
        return self.visited

    def __str__(self):
        output = ''
        for row in self.matrix:
            output += ' '.join(row) + '\n'
        return output

    def at_count(self, row, col, visited):
        if self.matrix[row][col] != '@':
            return 0

        visited[row][col] = True
        self.change_color(row, col)

        count = 1

        if row + 1 < self.height and not visited[row + 1][col]:
            visited[row + 1][col] = True
            count += self.at_count(row + 1, col, visited)

        if row - 1 >= 0 and not visited[row - 1][col]:
            visited[row - 1][col] = True
            count += self.at_count(row - 1, col, visited)

        if col + 1 < self.width and not visited[row][col + 1]:
            visited[row][col + 1] = True
            count += self.at_count(row, col + 1, visited)

        if col - 1 >= 0 and not visited[row][col - 1]:
            visited[row][col - 1] = True
            count += self.at_count(row, col - 1, visited)

        return count

    def change_color(self, row, col, color=Colors.GREEN):
        self.matrix[row][col] = color + self.matrix[row][col] + '\033[0m'


def main():
    m = Matrix(int(input('width?: ')), int(input('height?: ')))
    print()
    total_ats = 0
    for row in np.array(m.matrix):
        total_ats += (row == '@').sum()
    print('total @s:', total_ats)
    print(m.__str__())
    row = int(input('row?: '))
    col = int(input('column?: '))
    print()
    print('@s in blob:', m.at_count(row, col, m.get_visited()))
    print(m.__str__())


if __name__ == '__main__':
    main()
