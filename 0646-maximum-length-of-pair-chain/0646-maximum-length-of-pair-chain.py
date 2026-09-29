class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        n = len(pairs)
        pairs.sort( key = lambda x : x[1])
        print(pairs)
        if n == 1:
            return 1

        last = pairs[0][1]
        count = 1
        for start, end in pairs[1:]:
            if last < start:
                count += 1
                last = end
        return count
