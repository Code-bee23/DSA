import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        res = [[float('inf')]* m for _ in range(n)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        res[0][0] = grid[0][0]
        pq = [(grid[0][0],0,0)]

        def valid(i,j):
            return 0<=i<n and 0<=j<m

        while pq:
            money,row,col = heapq.heappop(pq)

            if money > res[row][col]:
                continue

            if row == n-1 and col == m-1:
                return money

            for k in range(4):
                r = row + dx[k]
                c = col + dy[k]

                if not valid(r,c):
                    continue

                new_wt = max(money,grid[r][c])

                if new_wt < res[r][c]:
                    res[r][c] = new_wt

                    heapq.heappush(pq,(new_wt,r,c))


        return -1