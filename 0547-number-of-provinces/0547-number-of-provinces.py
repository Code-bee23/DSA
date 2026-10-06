class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        prov = 0
        n = len(isConnected)
        vis = [False]*n

        def dfs(city):
            vis[city] = True
            for j in range(n):

                if isConnected[city][j] == 1 and not vis[j]:
                    dfs(j)

        for i in range(n):
            if not vis[i]:
                prov += 1
                dfs(i)

        return prov