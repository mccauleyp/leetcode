'''
https://leetcode.com/problems/number-of-islands/
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(i, j):
            neighbors = []
            if i - 1 >= 0: neighbors.append([i-1, j])
            if i + 1 < len(grid): neighbors.append([i+1, j])
            if j - 1 >= 0: neighbors.append([i, j-1])
            if j + 1 < len(grid[0]): neighbors.append([i, j+1])
            return neighbors
        
        def scan_island(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            neighbors = get_neighbors(i, j)
            for x, y in neighbors:
                scan_island(x, y)
                    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    scan_island(i, j)
        
        return count