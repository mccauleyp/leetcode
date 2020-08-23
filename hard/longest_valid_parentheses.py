'''
https://leetcode.com/problems/longest-valid-parentheses/
32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:  
        def scan_string(reverse=False):
            if not reverse:
                loop = range(0, len(s), 1)
                open_par = '('
            else:
                loop = range(len(s)-1, -1, -1)
                open_par = ')'
        
            output, left, right = 0, 0, 0

            for i in loop:
                if s[i] == open_par: left += 1
                else: right += 1

                if left == right:
                    output = max(output, left + right)          

                if right > left:
                    left, right = 0, 0
                    
            return output
        
        return max(scan_string(), scan_string(reverse=True))
'''
# Brute force solution (times out for very long input)
    def longestValidParentheses(self, s: str) -> int:
        output = 0
        for i in range(0,len(s)-1):
            if output >= len(s) - i:
                break
            open_p = 0
            close_p = 0
            for j in range(i, len(s)):
                if s[j] == '(':
                    open_p += 1
                if s[j] == ')':
                    if open_p == 0:
                        break
                    open_p -= 1
                
                if open_p == 0:
                    span = j - i + 1
                    if span > output:
                        output = span
        
        return output
