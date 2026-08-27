class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        n = len(s)

        # count frequency

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        # Try to match char left -- right

        match_ = 0

        while match_ < n:
            x = ord(target[match_]) - ord('a')

            if freq[x] == 0:
                break
            freq[x] -= 1
            match_ += 1
        
        # Try positions from right to left 

        for i in range(match_, -1, -1):

            if i < match_:
                x = ord(target[i]) - ord('a')
                freq[x] += 1
            
            if i < n:

                # find the slightly grater one 

                x = ord(target[i]) - ord('a')

                for c in range(x + 1, 26):

                    if freq[c] > 0:
                        freq[c] -= 1
                    
                        # prefix + chosen larger charcter
                        ans = target[:i] + chr( ord('a') + c)

                        # add remaing chars in acending order ( this will not affect the solution )

                        for j in range(26):
                            ans += chr( ord('a') + j) * freq[j]
                        return ans
        return ""
                

            
        
