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

            # main case ---> increase the level
            if index > 0 and index % 8 == 0:
                level += 1

            
            return freqs[index] * level + dfs(index + 1, level) 

        n = len(word)
        freq = {}
        
        for char in word:
            freq[char] = freq.get(char, 0)+1
        
        freqs = sorted( freq.values(), reverse = True)

        return dfs(0, 1)
