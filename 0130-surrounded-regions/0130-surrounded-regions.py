class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def valid(i,j):
            return 0<=i<n and 0<=j<m

        def dfs(i,j):
            board[i][j] = "#"

            for k in range(4):
                r = i + dx[k]
                c = j + dy[k]

                if valid(r,c) and board[r][c] == "O":
                    dfs(r,c)
            return

        for j in range(m):
            if board[0][j] == "O":
                dfs(0,j)

        for i in range(n):
            if board[i][0] == "O":
                dfs(i,0)
                       
        for j in range(m):
            if board[n-1][j] == "O":
                dfs(n-1,j)

        for i in range(n):
            if board[i][m-1] == "O":
                dfs(i,m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return