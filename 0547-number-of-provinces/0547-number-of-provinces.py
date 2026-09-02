class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            visited[node] = True

            for neighbour in range(V):
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)
            

        V = len(isConnected)
        

        visited = [False] * V
        provinces = 0

        for node in range(V):
            if not visited[node]:
                provinces += 1
                dfs(node)

        return provinces
