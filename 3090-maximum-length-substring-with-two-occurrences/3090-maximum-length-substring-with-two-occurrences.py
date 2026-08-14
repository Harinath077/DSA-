class Solution:
    # sliding window
    # expanad : untill reach the 2 occurances
    # shrink : if reached the 2 occurances

    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        left = 0
        right = 0
        mapp = defaultdict(int)
        maxLen = -1
        while right < n:

            mapp[s[right]] = mapp.get(s[right], 0) + 1

            while mapp[s[right]] > 2:
                mapp[s[left]] -= 1

                if mapp[s[left]] == 0:
                    del mapp[s[left]]
                left += 1
            
            if mapp[s[right]] <= 2:
                maxLen = max( maxLen, right - left + 1)
                
            right += 1
        return maxLen

                

