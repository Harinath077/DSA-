class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs( node ):
            visited[node] = True
            pathVisited[node] = True
            check[node] = False

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        check[node] = False
                        return True
                elif( pathVisited[neighbour] ):
                    check[neighbour] = False
                    return True
            
            # backtracking
            pathVisited[node] = False
            check[node] = True
            return False


        V = len(graph)
        visited = [False] * V
        check = [False] * V
        pathVisited = [False] * V
        safeSates = []
        
        for node in range(V):
            if not visited[node]:
                dfs(node)
        
        for i in range(V):
            if( check[i] ):
                safeSates.append(i)
        
        return safeSates