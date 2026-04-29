class Solution:
    def isCycle(self, V, adjList):
        def dfs(node):
            visited[node] = True
            pathVisited[node] = True
            # travesre using adj list
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif pathVisited[neighbor]:
                    return True
                
            # backTracking
            pathVisited[node] = False
            return False
        
        visited = [False] * V
        pathVisited = [False] * V
        # component vise Traversal
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct adjList
        adjList = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adjList[v].append(u)
        return not self.isCycle(numCourses, adjList)