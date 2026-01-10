class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        prev = [0] * (m + 1)

        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = ord(s1[i - 1]) + prev[j - 1]
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev = curr

        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)

        return total - 2 * prev[m]
