class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapp1 = defaultdict(int)
        mapp2 = defaultdict(int)
        for ch in word:
            if ch.islower():
                mapp1[ch] += 1
            else:
                mapp2[ch] += 1
        
        count = 0
        for key, val in mapp1.items():
            
            if(val >= 1 and mapp2[key.upper()] >= 1):
                count += 1
        return count