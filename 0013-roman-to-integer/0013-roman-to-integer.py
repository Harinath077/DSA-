class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        n = len(s)
        i = 0
        summ = 0
        while i < n:
            if i < n-1 and symbol[s[i]] < symbol[s[i+1]]:
                summ += symbol[s[i+1]] - symbol[s[i]]
                i += 2
            else:
                summ += symbol[s[i]]
                i += 1
        return summ

        