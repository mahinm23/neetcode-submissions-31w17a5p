class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        print(nums)
        num_set = set(nums)
        count = 1
        max_num = 1
        seen = set()

        for num in nums:
            if num in seen:
                continue
            if num + 1 in num_set:
                count += 1
                max_num = max(count, max_num)
                seen.add(num)
            
            else:
                count = 1
        
        return max_num