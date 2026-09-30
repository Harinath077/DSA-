class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # minHeap logic

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        minHeap = []
        for key, value in freq.items():
            heapq.heappush( minHeap, (value, key))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [key for val, key in minHeap]        