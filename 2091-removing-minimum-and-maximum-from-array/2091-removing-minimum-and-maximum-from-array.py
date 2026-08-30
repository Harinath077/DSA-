class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        def search(left, right, target):
            skips = 0

            for i in range(left, right):
                skips += 1

                if nums[i] == target:
                    return skips

        def searchB(right, left, target):
            skips = 0

            for i in range(right, left, -1):
                skips += 1

                if nums[i] == target:
                    return skips

        n = len(nums)

        min_ = min(nums)
        max_ = max(nums)

        minIndex = nums.index(min_)
        maxIndex = nums.index(max_)

        # 1. Delete only from FRONT
        cnt1 = search(0, n, min_)
        cnt2 = search(0, n, max_)
        delt1 = max(cnt1, cnt2)

        # 2. Delete only from BACK
        cntB1 = searchB(n - 1, -1, min_)
        cntB2 = searchB(n - 1, -1, max_)
        delt2 = max(cntB1, cntB2)

        
        # 3. Delete from FRONT and BACK
        # Option A:
        # min from front + max from back
        option1 = (
            search(0, n, min_) +
            searchB(n - 1, -1, max_)
        )

        # Option B:
        # max from front + min from back
        option2 = (
            search(0, n, max_) +
            searchB(n - 1, -1, min_)
        )

        delt3 = min(option1, option2)


        return min(delt1, delt2, delt3)