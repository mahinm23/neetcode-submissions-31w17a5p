class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        max_water = 0
        cur = 0

        while left < right:
            length = right - left
            # right is smaller, so contains water to that height
            if heights[left] > heights[right]:
                cur = heights[right] * length
                right -= 1
            # left is smaller, so contains water to that height
            else:
                cur = heights[left] * length
                left += 1
            max_water = max(cur, max_water)
            print(cur)
        
        return max_water
        