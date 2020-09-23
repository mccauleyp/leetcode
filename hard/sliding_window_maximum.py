'''
https://leetcode.com/problems/sliding-window-maximum/
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        left = [0]*length
        right = [0]*length
        
        left[0] = nums[0]
        for i in range(1, length):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max([left[i-1], nums[i]])
        
        right[-1] = nums[-1]
        for j in range(length-2, -1, -1):
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        
        output = []
        for i in range(0, length - k + 1):
            output.append(max([left[i+k-1], right[i]]))
            
        return output
'''
#Brute force:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(0, len(nums) - k + 1):
            current_max = nums[i]
            for j in range(i + 1, i + k):
                if nums[j] > current_max:
                    current_max = nums[j]
            output.append(current_max)
        return output