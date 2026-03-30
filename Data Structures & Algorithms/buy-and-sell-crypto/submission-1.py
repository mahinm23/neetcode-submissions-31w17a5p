class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_prof = 0
        curr_prof = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curr_prof = prices[right] - prices[left]
                max_prof = max(max_prof, curr_prof)
            else:
                left = right

            right += 1
             
        return max_prof