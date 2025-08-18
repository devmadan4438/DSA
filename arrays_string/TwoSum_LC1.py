# TOPIC: Two pointer

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i in range(len(nums)):
            nextNum = target - nums[i]
            
            if nextNum in seen:
                return [seen[nextNum], i] 

            seen[nums[i]] = i
