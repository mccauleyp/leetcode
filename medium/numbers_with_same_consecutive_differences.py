'''
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
967. Numbers With Same Consecutive Differences
Medium

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

 

Note:

    1 <= N <= 9
    0 <= K <= 9
'''
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]: 
        output = []
        
        def build_entry(seed):
            if len(seed) == N:
                output.append(int(seed))
                return 
            
            solns = [int(seed[-1]) + k for k in [-K, K]]
            if solns[0] == solns[1]: solns.pop()
                
            for soln in solns:
                if soln >= 0 and soln <= 9:
                    build_entry(seed + str(soln))
        
        start = 0 if N == 1 else 1
        for i in range(start, 10):
            build_entry(str(i))
            
        return output