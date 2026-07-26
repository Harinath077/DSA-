from collections import defaultdict
from typing import List

class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD = 10**9 + 7

        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)

        # Empty partition:
        # before taking any element, we are ready to build
        # the first block (which must be target1).
        cnt2[0] = 1

        pre = 0
        ans = 0

        for x in nums:
            pre ^= x

            # Ways to end the current block with target1
            a = cnt2[pre ^ target1]

            # Ways to end the current block with target2
            b = cnt1[pre ^ target2]

            ans = (a + b) % MOD

            cnt1[pre] = (cnt1[pre] + a) % MOD
            cnt2[pre] = (cnt2[pre] + b) % MOD

        return ans