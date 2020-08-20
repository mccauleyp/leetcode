'''
https://leetcode.com/problems/longest-common-prefix
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        if len(strs) == 0:
            return output
        if len(strs) == 1:
            return strs[0]
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if i > len(strs[j]) -1 or strs[j][i] != strs[0][i]:
                    return output
            output += strs[0][i]
        
        return output
