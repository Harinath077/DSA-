import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                remaining = heapq.heappop(max_heap) + 1
                if remaining:
                    cooldown.append((remaining, time + n))

            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time