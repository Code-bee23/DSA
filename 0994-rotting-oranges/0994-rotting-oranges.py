from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        q = deque()
        fresh = 0

        # Put all rotten oranges in queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q and fresh > 0:

            size = len(q)

            for _ in range(size):
                i, j = q.popleft()

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1