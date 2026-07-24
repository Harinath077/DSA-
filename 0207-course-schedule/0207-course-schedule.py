class Solution:
    def isCycle(self, V, adjList):
        
        def dfs(node):

            visited[node] = True
            pathVisited[node] = True

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
                elif pathVisited[neighbour] == True:
                    return True
            
            # backtracking
            pathVisited[node] = False
            return False

        visited = [False] * V
        pathVisited = [False] * V

        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return True
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]

        # building the adjList
        for u, v in prerequisites:
            adjList[v].append(u)
        
        return not self.isCycle(numCourses, adjList)