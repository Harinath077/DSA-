class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # using freq[s] as a key
        anagramMap = {}

        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)

            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        
        return list(anagramMap.values())
            