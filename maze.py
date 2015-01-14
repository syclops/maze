"""
:mod:`maze` --- Maze creation
=============================

All necessary functionality for creating mazes.
"""

import fileinput

class Room(object):
    """
    Single room that player navigates.
    """

    def __init__(self, type=' '):
        self.type = type
        self.visited = False

class Maze(object):
    """
    Maze that player navigates.
    """

    def __init__(self, mazeFile):
        self.height = None
        self.width = None
        i = 0
        for line in fileinput.input(mazeFile):
            if self.height is None or self.width is None:
                [self.height, self.width] = map(int, line.strip().split())
                self.array = [[Room() for j in range(self.width)] for i in
                              range(self.height)]
            else:
                j = 0
                for char in line.strip():
                    if char == 'S':
                        self.player_row = i
                        self.player_col = j
                    self.array[i][j] = Room(char)
                    j += 1
                i += 1

    def __repr__(self):
        outStr = ''
        for i in range(self.height):
            for j in range(self.width):
                outStr += self.array[i][j].type
            outStr += '\n'
        return outStr
