'''
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists
Hard

Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 

Constraints:

    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Solution using heapq to do the sorting
class Solution:
    from heapq import heappush, heappop
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for this_list in lists:
            current = this_list
            while current:
                heappush(heap, current.val)
                current = current.next
        
        tmp_head = ListNode(42)
        current = tmp_head
        while heap:
            current.next = ListNode(heappop(heap))
            current = current.next
            
        return tmp_head.next
'''
# Solution that iteratively compares the heads of each list, much slower than the 
# heap sort method above. 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tmp_head = ListNode(42)
        current = tmp_head
        
        while None in lists: lists.remove(None)
        
        while lists:
            index = 0
            next_node = lists[0]
            for i in range(0, len(lists)):
                if lists[i].val < next_node.val:
                    next_node = lists[i]
                    index = i
                
            current.next = next_node
            current = current.next
            
            lists[index] = lists[index].next
            if not lists[index]:
                lists.pop(index)
            
        return tmp_head.next
        
        
        