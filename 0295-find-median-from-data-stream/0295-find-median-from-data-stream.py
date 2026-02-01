import heapq
class MedianFinder:

    def __init__(self):
        self.small = []  # Max-heap (simulated using negatives)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Always push to large first
        heapq.heappush(self.large, num)

        # Step 2: Ensure the smallest number in 'large' is not less than the largest in 'small'
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

        # Step 3: Balance the heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()