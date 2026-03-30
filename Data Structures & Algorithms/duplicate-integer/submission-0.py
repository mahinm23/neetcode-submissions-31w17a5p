class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for item in nums:
            print(item)
            if item in my_dict:
                my_dict[item] += 1
                return True
            else:
                my_dict[item] = 1
        
        return False

