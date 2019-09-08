"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque


DIRECTIONS = [(-2, -1), (-2, 1), (-1, 2), (1, 2),
              (2, 1), (2, -1), (1, -2), (-1, -2)]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        queue = deque([(source.x, source.y)])
        distances = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distances[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distances:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue
                distances[(next_x, next_y)] = distances[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1

    def is_valid(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and not grid[x][y]
