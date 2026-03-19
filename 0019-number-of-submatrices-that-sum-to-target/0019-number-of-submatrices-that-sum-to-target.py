class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for r1 in range(rows):
            compress = [0] * cols          # column sums between r1 and r2

            for r2 in range(r1, rows):
                # Extend the compressed array by including row r2
                for c in range(cols):
                    compress[c] += matrix[r2][c]

                # Now solve: how many subarrays of 'compress' sum to target?
                # Classic prefix sum + hashmap trick (LeetCode 560)
                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                prefix_sum = 0

                for val in compress:
                    prefix_sum += val
                    # If (prefix_sum - target) was seen before,
                    # those are valid left boundaries
                    count += prefix_count[prefix_sum - target]
                    prefix_count[prefix_sum] += 1

        return count