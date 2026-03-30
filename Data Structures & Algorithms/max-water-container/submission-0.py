class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height_lim = min(heights[left], heights[right])
            curr_area = width * height_lim

            max_area =max(max_area, curr_area)

            # discard bottleneck boundary
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area