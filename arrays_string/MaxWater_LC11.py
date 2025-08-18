# TOPIC: Two pointer

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = float('-inf')

        while left < right:
            contained_water = (right - left) * min(height[left], height[right])

            if contained_water > max_water:
                max_water = contained_water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
            

       
        