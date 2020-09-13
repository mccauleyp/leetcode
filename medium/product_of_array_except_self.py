'''
https://leetcode.com/problems/product-of-array-except-self/
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
# Constant space solution: 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1]*length

        for i in range(1, length):
            output[i] = output[i-1]*nums[i-1]
                
        running_product = 1
        for i in range(length-1, -1, -1):
            if i < length-1:
                running_product *= nums[i+1]
            output[i] *= running_product
            
        return output
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1]*length
        left_product = output.copy()
        right_product = output.copy()
        
        for i in range(1, length):
            left_product[i] = left_product[i-1]*nums[i-1]
                
        for i in range(length-2, -1, -1):
            right_product[i] = right_product[i+1]*nums[i+1]
        
        for i in range(0, length):
            output[i] = left_product[i]*right_product[i]
        
        return output
'''
'''
# This solution uses division and won't work if there are 0s in the array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        for num in nums:
            total_product *= num
        output = [total_product]*len(nums)
        for i, num in enumerate(nums):
            output[i] = output[i]//num
        return output
'''