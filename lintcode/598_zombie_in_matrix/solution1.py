import collections


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        days = 0
        while q:
            size = len(q)
            days += 1
            for k in range(size):
                i, j = q.popleft()
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for di, dj in dirs:
                    next_i = i + di
                    next_j = j + dj
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    if grid[next_i][next_j] == 1 or grid[next_i][next_j] == 2:
                        continue
                    grid[next_i][next_j] = 1
                    q.append((next_i, next_j))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
        return days - 1
