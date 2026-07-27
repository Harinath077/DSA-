class Solution:

    MOD = 10**9 + 7

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # build the graph
        adjList = [[] for _ in range(n)]
        for u, v, wt in roads:
            adjList[u].append( (v, wt) )
            adjList[v].append( (u, wt) )
        
        # declare DS 
        minHeap = []
        dist = [float('inf')] * n
        ways = [-1] * n
        
        dist[0] = 0
        heapq.heappush( minHeap, (0, 0))
        ways[0] = 1
        
        # dijkstra's algo
        while minHeap:
            
            currDist, currNode = heapq.heappop( minHeap )
            
            if currDist > dist[currNode]:
                continue
            
            for adjNode, edgeDist in adjList[currNode]:
                newDist = edgeDist + currDist
                
                if newDist < dist[adjNode]:
                    dist[adjNode] = newDist
                    heapq.heappush( minHeap, (newDist, adjNode))
                    ways[adjNode] = ways[currNode]
                
                elif newDist == dist[adjNode]:
                    ways[adjNode] =  (ways[currNode] + ways[adjNode]) % self.MOD
        
        return ways[n-1]