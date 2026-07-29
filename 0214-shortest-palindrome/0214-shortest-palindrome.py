class Solution:
    """  
    The problem is depends of the orders of the character not on frequency
    
    so find the longest prefix palindrome
    and the suffix of it 
    and the reverse of it
    and add in front 

    Eg : aacecaaa

    longest prefix palidrome is : aacecaa
    suffix : a

    revser(suffix) = a
    add to front : a + aacecaaa


    """
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        # edge case 
        if n <= 1 or s == s[::-1]:
            return s
        
        right = n-1
        splitP = 0
        while right >= 0:
            prefix = s[:right]
    
            if prefix == prefix[::-1]:
                splitP = right
                break
            right -= 1

        prefix_ = s[:splitP]
        suffix = s[splitP:]
        ans = suffix[::-1] + s
        return ans
        