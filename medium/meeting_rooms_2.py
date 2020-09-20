'''
https://leetcode.com/problems/meeting-rooms-ii/
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        intervals.sort()
        heap = [(intervals[0][1], intervals[0])]
        output = 1
        
        for interval in intervals[1:]:
            if heap[0][0] <= interval[0]:
                heapq.heapreplace(heap, (interval[1], interval))
            else:
                heapq.heappush(heap, (interval[1], interval))
                if len(heap) > output:
                    output = len(heap)

        return output