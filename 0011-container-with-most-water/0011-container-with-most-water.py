class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxArea = 0
        while left < right:
            height_ = min(height[left], height[right])
            width = right - left
            area = height_ * width
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea
        