class Solution:
    def checkPartitioning(self, s: str) -> bool:
        
        def isPalindrome( start, end ):

            while ( start < end ):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        
        def dfs(index, count):

            # base case
            
            if count == 3:
                return index == n
            
            if memo[index][count] != -1:
                return memo[index][count]
                
            for j in range(index, n):

                if palindrome[index][j]:
                    if dfs(j+1, count + 1):
                        memo[index][count] = True
                        return memo[index][count]
            
            memo[index][count] = False
            return memo[index][count]
        
        n = len(s)
        # palindrome precomputation
        palindrome = [[False] * n for _ in range(n)]

        for start in range(n-1, -1, -1):
            for end in range(start, n):

                if s[start] == s[end]:
                    # base case 
                    if end - start <= 1:
                        palindrome[start][end] = True
                    else:
                        palindrome[start][end] = palindrome[start+1][end-1]

        memo = [[-1] * 4 for _ in range(n+1)]
        return dfs(0, 0)

