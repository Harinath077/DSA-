class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
            for neighbour in adj[node]:
                if( not visited[neighbour]):
                    dfs(neighbour)

        def buildAdjList():
            addList = [[] for _ in range(V)]
            for i in range(V):
                for j in range(V):
                    if( isConnected[i][j] == 1):
                        addList[i].append(j)
                        addList[j].append(i)
            return addList

        V = len(isConnected)
        visited = [False] * V
        adj = buildAdjList()
        provinces = 0 

        for node in range(V):
            if( not visited[node] ):
                provinces += 1
                dfs(node)
        return provinces