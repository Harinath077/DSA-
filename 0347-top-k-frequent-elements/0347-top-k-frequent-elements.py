class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # maxHeap logic

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        maxHeap = []
        for key, value in freq.items():
            heapq.heappush( maxHeap, (-value, key))
        
        res = []
        for _ in range(k):
            res.append( maxHeap[0][1])
            heapq.heappop(maxHeap)
        
        return res

        