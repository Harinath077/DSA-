from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        # heapifying
        heapq.heapify( maxHeap )

        time = 0
        coolDown = deque()

        while( maxHeap or coolDown ):
            time += 1

            if( maxHeap ):
                remaining = 1 + heapq.heappop(maxHeap)

                if( remaining ): # have still task to complete
                    coolDown.append( (remaining, time + n))
            
            # Push back tasks whose cooldown finished
            if( coolDown and coolDown[0][1] <= time):
                remainingFreq, _ = coolDown.popleft()
                heapq.heappush( maxHeap, remainingFreq )

        return time

