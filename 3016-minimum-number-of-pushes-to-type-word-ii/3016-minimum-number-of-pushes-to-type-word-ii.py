class Solution:
    """  
    here frequency needed
    freq[char] * level

    """
    def minimumPushes(self, word: str) -> int:
        def dfs(index, level):
            # base case
            if index >= len(freqs):
                return 0

            cost = 0
            for i in range(index, min(index + 8, len(freqs))):
                cost += freqs[i] * level
            
            return cost + dfs(index + 8, level + 1)

        n = len(word)
        freq = {}
        
        for char in word:
            freq[char] = freq.get(char, 0)+1
        
        freqs = sorted( freq.values(), reverse = True)

        return dfs(0, 1)
