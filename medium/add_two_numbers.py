'''
https://leetcode.com/problems/add-two-numbers
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = str(l1.val)
        current = l1
        while current.next:
            s1 = str(current.next.val)+s1
            current = current.next
        
        s2 = str(l2.val)
        current = l2
        while current.next:
            s2 = str(current.next.val)+s2
            current = current.next
        
        total = str(int(s1)+int(s2))
        
        head = ListNode(int(total[-1]))
        current = head
        for i in range(len(total)-2, -1, -1):
            current.next = ListNode(int(total[i]))
            current = current.next
            
        return head
            
            