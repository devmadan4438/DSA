# [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution(object):
    def trap(self, height):
        if len(height) == 0: 
            return
            
        left, right = 0, len(height) - 1
        left_max , right_max = height[left], height[right]
        trap_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trap_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trap_water += right_max - height[right]

        return trap_water

      