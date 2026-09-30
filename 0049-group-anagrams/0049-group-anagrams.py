class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramMap = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagramMap:
                anagramMap[sorted_s] = []
            anagramMap[sorted_s].append(s)

        return [*anagramMap.values()]
            