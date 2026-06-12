class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            need = target-num
            if need in nums_dict:
                return [nums_dict[need], idx]
            nums_dict[num] = idx

        