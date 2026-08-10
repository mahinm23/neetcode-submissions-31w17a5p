class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = []
        front = 0

        while front in range(len(nums)):
            if front > 0 and nums[front] == nums[front-1]:
                front += 1
                continue
            
            left = front + 1
            right = len(nums)-1

            while left < right:
                sum = nums[left] + nums[right]
                if sum == -nums[front]:
                    sols.append([nums[front], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1

                elif sum < -nums[front]:
                    left += 1
                elif sum > -nums[front]:
                    right -= 1
            
            front += 1
        
        return list(sols)