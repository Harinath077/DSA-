class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0] * (m + 1)  # Initialize with zeros

        for ind1 in range(1, n + 1):
            curr = [0] * (m + 1)  # Initialize curr with zeros for each new row
            for ind2 in range(1, m + 1):
                # match
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                # not match
                else:
                    curr[ind2] = max(curr[ind2 - 1], prev[ind2])
            prev = curr

        return prev[m]  # Return the value at prev[m]
