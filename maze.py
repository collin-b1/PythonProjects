from random import randrange


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze_matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # self.create_maze(self.width // 2, self.height // 2)
        self.create_maze(1, 1)

    def __str__(self):
        string = ""
        for x in self.maze_matrix:
            for y in x:
                string += "\u2588\u2588" if y == 0 else "  "
            string += "\n"
        return string

    def create_maze(self, x, y):
        if self.is_open(x, y):
            self.change_state(x, y, 1)

        states = [False] * 4
        if self.is_open(x + 2, y) and self.is_open(x + 1, y):
            states[0] = True
        if self.is_open(x - 2, y) and self.is_open(x - 1, y):
            states[1] = True
        if self.is_open(x, y + 2) and self.is_open(x, y + 1):
            states[2] = True
        if self.is_open(x, y - 2) and self.is_open(x, y - 1):
            states[3] = True
        if True in states:
            rand = randrange(4)
            if rand == 0 and states[0]:
                self.change_state(x + 1, y)
                self.create_maze(x + 2, y)
            elif rand == 1 and states[1]:
                self.change_state(x - 1, y)
                self.create_maze(x - 2, y)
            elif rand == 2 and states[2]:
                self.change_state(x, y + 1)
                self.create_maze(x, y + 2)
            elif rand == 3 and states[3]:
                self.change_state(x, y - 1)
                self.create_maze(x, y - 2)

            self.create_maze(x, y)

    def is_open(self, x, y):
        return not x >= len(self.maze_matrix[0]) and not x < 0 and \
               not y >= len(self.maze_matrix) and not y < 0 and \
               self.maze_matrix[y][x] == 0

    def change_state(self, x, y, state=1):
        self.maze_matrix[y][x] = state


def main():
    maze = Maze(int(input('width?: ')), int(input('height?: ')))
    print(maze.__str__())


if __name__ == "__main__":
    try:
        main()
    except RecursionError:
        print("maximum recursion depth error")
