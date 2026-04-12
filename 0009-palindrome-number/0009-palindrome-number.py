class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        orginal = x
        reversed_num = 0
        while x>0:
            reversed_num = reversed_num * 10
            reversed_num += x % 10
            x = x//10
        return orginal == reversed_num


        
        