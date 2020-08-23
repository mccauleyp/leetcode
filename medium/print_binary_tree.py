'''
https://leetcode.com/problems/print-binary-tree/
655. Print Binary Tree
Medium

Print a binary tree in an m*n 2D string array following these rules:

    The row number m should be equal to the height of the given binary tree.
    The column number n should always be an odd number.
    The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
    Each unused space should contain an empty string "".
    Print the subtrees following the same rules.

Example 1:

Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

Example 3:

Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note: The height of binary tree is in the range of [1, 10]. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(root):
            if not root:
                return 0
            return 1 + max(get_depth(root.left), get_depth(root.right))
    
        depth = get_depth(root)
        width = 2**depth - 1
        output = [['' for j in range(width)] for i in range(depth)]
        
        parent_ind = width//2
        output[0][parent_ind] = str(root.val)
        
        def fill_out(node, parent_ind, level):
            if not node:
                return
            spacing = 2**(depth - 1 - level)
            ind = parent_ind - spacing
            if node.left:
                output[level][ind] = str(node.left.val)
            fill_out(node.left, ind, level+1)
            
            ind = parent_ind + spacing
            if node.right:
                output[level][ind] = str(node.right.val)
            fill_out(node.right, ind, level+1)
        
        fill_out(root, parent_ind, 1)
            
        return output