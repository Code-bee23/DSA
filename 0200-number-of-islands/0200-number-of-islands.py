class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def valid(i,j):
            return 0<=i<n and 0<=j<m

        def dfs(i,j):
            vis[i][j] = 1

            for k in range(4):
                row = i + dx[k]
                col = j + dy[k]

                if (valid(row,col) and grid[row][col] =='1' and vis[row][col] ==0):

                    dfs(row,col)
        res = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    res += 1
                    dfs(i,j)
        return res