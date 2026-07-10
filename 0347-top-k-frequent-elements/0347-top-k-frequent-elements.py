class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_heap = []
        ans = []
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for key, val in freq.items():
            heapq.heappush(max_heap, (-val, key))
        
        for _ in range(k):
            ans.append( heapq.heappop(max_heap)[1])
        
        return ans


