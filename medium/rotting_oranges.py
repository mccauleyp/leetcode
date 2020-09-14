'''
https://leetcode.com/problems/rotting-oranges/
994. Rotting Oranges
Medium

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
'''
class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dimensions = [len(grid),len(grid[0])]
        if dimensions[0] == 1:
            grid.append([0 for i in range(len(grid[0]))])
            dimensions[0] = 2
            
        def valid_neighbors(row, col):
            neighbors = []
            if row - 1 >= 0: neighbors.append([row - 1, col])
            if row + 1 < dimensions[0]: neighbors.append([row + 1, col])
            if col - 1 >= 0: neighbors.append([row, col - 1])
            if col + 1 < dimensions[1]: neighbors.append([row, col + 1])
            return neighbors
        
        queue = deque()
        level = 0
        for row in range(dimensions[0]):
            for col in range(dimensions[1]):
                if grid[row][col] == 2:
                    grid[row][col] = 0
                    queue.appendleft([row, col, level])
        
        while queue:
            row, col, level = queue.pop()
            neighbors = valid_neighbors(row, col)
            for row, col in neighbors:
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.appendleft([row, col, level + 1])
        
        remaining = sum([value for row in grid for value in row])
        output = -1 if remaining > 0 else level
                                        
        return output