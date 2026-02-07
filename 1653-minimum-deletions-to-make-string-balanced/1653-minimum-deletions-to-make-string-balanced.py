class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                # Either delete this 'a' or delete all previous 'b's
                deletions = min(deletions + 1, b_count)

        return deletions