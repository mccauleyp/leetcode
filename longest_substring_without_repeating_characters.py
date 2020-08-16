'''
https://leetcode.com/problems/longest-substring-without-repeating-characters
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        output = 1
        j = 0 #left/catchup pointer
        chars = set(s[0])
        for i in range(1,len(s)):
            if s[i] not in chars:
                chars.add(s[i])
                if i-j+1 > output:
                    output = i-j+1
            else:
                while s[j] != s[i]:
                    chars.discard(s[j])
                    j += 1
                j += 1
                        
        return output