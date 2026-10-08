class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        res = True 
        n = len(graph)
        colors = [-1] * n
        
        def check(node,c):
            nonlocal res
            colors[node] = c
            
            for neigh in graph[node]:

                if colors[neigh] == -1:
                    if not check(neigh,1-c):
                        return False

                if colors[neigh] == c:
                    return False

            return True

        for i in range(n):
            if colors[i] == -1:
                if not check(i,0):
                    return False

        return True

