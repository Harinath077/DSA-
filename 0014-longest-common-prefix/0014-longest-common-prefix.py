class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        first = strs[0]
        last = strs[-1]
        min_ = min(len(first),len(last))
        while i < min_ and first[i] == last[i]:
            i += 1
        return first[:i]
        