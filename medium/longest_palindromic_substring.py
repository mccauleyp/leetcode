'''
https://leetcode.com/problems/longest-palindromic-substring
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:      
        length = len(s)
        max_pal = 0
        output = ''
        
        def grow_palindrome(left, right):
            while left-1 >= 0 and right+1 < length and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
            pal_len = right - left + 1 
            return pal_len, left, right
        
        for i in range(0, length):
            pal1 = grow_palindrome(i, i)
            if i+1 < length and s[i] == s[i+1]:
                pal2 = grow_palindrome(i,  i+1) 
            else:
                pal2 = (0, i, i+1)
            
            if pal1[0] > max_pal or pal2[0] > max_pal:
                if pal1[0] > pal2[0]:
                    left, right = pal1[1], pal1[2]
                else:
                    left, right = pal2[1], pal2[2]
                    
                output = s[left:right+1]
                max_pal = right - left + 1
        
        return output