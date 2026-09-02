class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            visited[node] = True

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        V = len(isConnected)
        # build the graph
        adjList = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        visited = [False] * V
        provinces = 0
        
        for node in range(V):
            if not visited[node]:
                provinces += 1
                dfs(node)
        
        return provinces


