from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        result = 0

        for top in range(rows):
            # Compress columns
            col_sums = [0] * cols

            for bottom in range(top, rows):
                # Update column sums
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                # Now count subarrays with sum = target
                prefix_sum = 0
                prefix_map = {0: 1}   # manual hashmap

                for val in col_sums:
                    prefix_sum += val

                    # Check if (prefix_sum - target) exists
                    if (prefix_sum - target) in prefix_map:
                        result += prefix_map[prefix_sum - target]

                    # Update hashmap manually
                    if prefix_sum in prefix_map:
                        prefix_map[prefix_sum] += 1
                    else:
                        prefix_map[prefix_sum] = 1

        return result