class Solution:
    def isValid(self, s: str) -> bool:
        # edge case 
        if len(s) == 1:
            return False
        mapping = {')':'(', ']':'[','}':'{'}
        stack = []
        
        for char in s:
            # opening para
            if char in mapping.values():
                stack.append(char)
            else: # opening para
                if stack and stack[-1] != mapping[char]:
                    return False
                elif stack:
                    stack.pop()
                else:
                    return False
        return not stack