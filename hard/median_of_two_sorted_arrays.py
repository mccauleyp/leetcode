'''
https://leetcode.com/problems/median-of-two-sorted-arrays
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        target = length//2 + 1 
        even = True if length%2 == 0 else False
        previous = None
        current = None
        i=0
        j=0
        while i+j < target:
            previous = current
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    current = nums1[i]
                    i += 1
                else:
                    current = nums2[j]
                    j += 1
            else:
                if i < len(nums1):
                    current = nums1[i]
                    i += 1
                else:
                    current = nums2[j]
                    j += 1
            
        return (current+previous)/2 if even else current
        
            
        
        