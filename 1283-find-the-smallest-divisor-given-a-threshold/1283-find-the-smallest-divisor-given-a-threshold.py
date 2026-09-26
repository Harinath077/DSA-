class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
            def sumComputation(divisor):
                sum_ = 0
                for num in nums:
                    sum_ += math.ceil(num / mid)       
                return sum_

            ans = -1
            low = 1
            high = max(nums)

            while low <= high:
                mid = low + (high - low) // 2                
                if sumComputation(mid) <= threshold:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans