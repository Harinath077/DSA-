class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        def reverse(left, right, arr):

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr
        n = len(nums)

        ans = [0] * n
        ptr = 0
        revPtr = n-1

        ans[ptr] = nums[0]
        ans[revPtr] = nums[1]
        print(ans)
        for i in range(2, n):
            if ans[ptr] > ans[revPtr]:
                ptr += 1
                ans[ptr] = nums[i]
            else:
                revPtr -= 1
                ans[revPtr] = nums[i]
        
        return reverse(revPtr, n-1, ans)