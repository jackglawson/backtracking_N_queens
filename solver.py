import numpy as np


class NQueensSolver:
    def __init__(self, size):
        self.size = size
        self.num_solutions = 0

    def solve(self):
        self.bt(self.root())

    def bt(self, c):
        """backtracking algorithm"""
        if self.reject(c):
            return
        if self.accept(c):
            self.output(c)
            return

        possible_spaces = self.get_possible_spaces(c)
        for possible_space in possible_spaces:
            c.add(possible_space)
            self.bt(c)
            c.remove(possible_space)

    def root(self):
        """the root of the backtracking tree"""
        return set()

    def reject(self, c):
        """return true only if the partial candidate c is not worth completing"""
        possible_spaces = self.get_possible_spaces(c)
        return True if len(possible_spaces) < self.size - len(c) else False

    def accept(self, c):
        """return true if c is a solution of P, and false otherwise"""
        return True if len(c) == self.size else False

    def output(self, c):
        print('SOLUTION FOUND: {}'.format(c))
        self.num_solutions += 1

    def get_possible_spaces(self, c):
        """returns coords of unnattacked squares.
        Will only give coords past the last queen, so the same solution doesnt occur again and again"""

        last_q = max(c) if c else (-1, -1)

        possible_spaces = {(i, j) for j in range(self.size) for i in range(self.size) if (i, j) > last_q}
        for q in c:
            # remove row:
            for col in range(self.size):
                possible_spaces.discard((q[0], col))

            # remove col:
            for row in range(self.size):
                possible_spaces.discard((row, q[1]))

            # remove diags:
            row, col = q
            while row <= self.size and col <= self.size:
                possible_spaces.discard((row, col))
                row += 1
                col += 1

            row, col = q
            while row <= self.size and col >= 0:
                possible_spaces.discard((row, col))
                row += 1
                col -= 1

            row, col = q
            while row >= 0 and col <= self.size:
                possible_spaces.discard((row, col))
                row -= 1
                col += 1

            row, col = q
            while row >= 0 and col >= 0:
                possible_spaces.discard((row, col))
                row -= 1
                col -= 1

        possible_spaces = list(possible_spaces)
        return possible_spaces


size = 8
solver = NQueensSolver(size)
solver.solve()
print(solver.num_solutions)
#I did something