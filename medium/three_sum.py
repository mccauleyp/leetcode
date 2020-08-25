'''
https://leetcode.com/problems/3sum/
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
#top solution doesn't require sorting list first
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        global_seen = set()  
        local_seen = {}
        for i in range(0, len(nums)-1):
            if nums[i] not in global_seen:
                global_seen.add(nums[i])
                for j in range(i+1, len(nums)):
                    complement = -(nums[i] + nums[j])
                    if complement in local_seen and local_seen[complement] == i:
                        soln = tuple(sorted([nums[i], nums[j], complement]))
                        output.add(soln)
                    local_seen[nums[j]] = i         
        return output
'''
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers)-1
    output = set()
    while left < right:
        if numbers[left] + numbers[right] == target:
            output.add((numbers[left], numbers[right]))
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    return tuple(output)    

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        output = set()
        nums.sort()
        seen = set()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if nums[i] not in seen:
                seen.add(nums[i])
                two_sums = twoSum(nums[i+1:], -nums[i])
                if two_sums:
                    for two_sum in two_sums:
                        soln = (nums[i],) + two_sum
                        output.add(soln)
        return output