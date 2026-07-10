class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        sorted_freq = dict(
            sorted(freq.items(), 
                    key = lambda item : item[1], 
                    reverse = True)
            )

        res = []
        i = 0
        for key in sorted_freq.keys():
            if( i == k):
                break
            res.append(key)
            i += 1

        return res

