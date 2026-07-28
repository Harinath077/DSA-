class Solution:
    """ 
    Bucker sorting technique
    """
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        bucket = [0] * 26
        partition = n // 2

        # frequency
        for i in range(partition):
            bucket[ ord(s[i]) - ord('a') ] += 1
        
        temp = []
        for i in range(26):
            if bucket[i] > 0:
                temp.append( chr(i + ord('a')) * bucket[i] )
                
        firstHalf = ''.join( temp )

        mid = ''
        if n % 2 == 1:
            mid = s[partition]
        
        secondHalf = firstHalf[::-1]

        return firstHalf + mid + secondHalf



