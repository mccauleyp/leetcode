'''
https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Accepted
543,052
Submissions
1,109,053
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)        
        if length == 0:
            return 0
        
        left = [0 for i in range(len(height))]
        right = left.copy()        
        
        current_wall = height[0]
        for i in range(1, length):
            if height[i-1] > current_wall:
                current_wall = height[i-1]
            left[i] = current_wall
        
        current_wall = height[-1]
        for i in range(length-2, -1, -1):
            if height[i+1] > current_wall:
                current_wall = height[i+1]
            right[i] = current_wall 
        
        output = 0
        for i in range(0, length):
            lower_wall = left[i] if left[i] < right[i] else right[i]
            if height[i] < lower_wall:
                output += lower_wall - height[i]
            
        return output 