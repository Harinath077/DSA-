class Solution:
    def checkPartitioning(self, s: str) -> bool:
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

        # partition DP
        dp = [[False] * (4) for _ in range(n+1)]

        # base case
        dp[n][3] = True

        for index in range(n-1, -1, -1):
            for count in range(2, -1, -1):
                for j in range(index, n):

                    if palindrome[index][j]:
                        if dp[j+1][count + 1]:
                            dp[index][count] = True
                            break
            
        return dp[0][0]

