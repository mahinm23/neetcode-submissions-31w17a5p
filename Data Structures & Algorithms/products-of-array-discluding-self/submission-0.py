class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        out_arr = [1]*length

        prefix = 1
        for i in range(0, length):
            out_arr[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(length-1, -1, -1):
            out_arr[i] = out_arr[i] * suffix
            suffix = suffix * nums[i]

        return out_arr