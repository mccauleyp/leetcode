'''
https://leetcode.com/problems/zigzag-conversion
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        length = len(s) 
        step = 2*numRows - 2
        output = ''
        
        for i in range(0, numRows):
            for j in range(i, length, step):
                output += s[j]
                if i != numRows-1 and i != 0 and j+step-2*i < length:
                    output += s[j+step-2*i]
        
        return output
'''
# Suboptimal solution here that just populates a matrix and converts to a string
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        length = len(s)
        column = ['']*numRows
        matrix = []
        output = ''
        
        this_column = column.copy()
        j = 0
        diagonal = False
        for i in range(0,length):
            if not diagonal:
                if j < numRows:
                    this_column[j] = s[i]
                    j += 1
                    addcol = True if i == length - 1 else False
                else:
                    addcol = True
                    diagonal = True
                    j = numRows-2
                if addcol: matrix.append(this_column)
            
            if diagonal:
                this_column = column.copy()
                this_column[j] = s[i]
                if j > 0 and numRows > 2:
                    addcol = True
                    j -= 1
                else:
                    addcol = True if i == length - 1 else False                 
                    diagonal = False
                    j += 1
                if addcol: matrix.append(this_column)
                
        for i in range(0, len(column)):
            for j in range(0,len(matrix)):
                output += matrix[j][i]
            
        return output
'''