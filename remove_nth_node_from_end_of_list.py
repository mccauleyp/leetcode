'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Single Pass Solution:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        link1 = head     
        link2 = link1.next
        count = 1
        while node.next:
            if count >= n+1:
                link1 = link1.next
                link2 = link2.next
            node = node.next
            count += 1
        
        if count == 1:
            return None       
        if count - n == 0:
            return head.next
        if count == 2:
            head.next = None
            return head 
                
        link1.next = link2.next
        return head
'''
# Double Pass Solution:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def get_length(head):
            if not head.next:
                return 1
            return 1 + get_length(head.next)
        
        length = get_length(head)
        
        if length == 1:
            return None
        
        if length - n == 0:
            return head.next
        
        count = 1
        current = head
        while count < length-n:
            current = current.next
            count += 1

        current.next = current.next.next
                     
        return head