class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch,0)+1
            
        instances = len(text)
        for ch in "balloon":
            if( ch not in freq or not (freq['l'] >= 2 and freq['o'] >= 2 ) ):
                return 0
            else:
                if( ch == "l" or ch == "o" ):
                    actualFreq = freq[ch] // 2
                else:
                    actualFreq = freq[ch]
                
                if( actualFreq < instances):
                    instances = actualFreq
            
                
            
        
        return instances
