'''
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
Hard

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

 

Follow up:

    If all integer numbers from the stream are between 0 and 100, how would you optimize it?
    If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''
from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = [] #max heap of smaller half values
        self.larger = [] #min heap of larger half values

    def addNum(self, num: int) -> None:
        if len(self.larger) == 0:
            heappush(self.larger, num)
        elif len(self.smaller) == 0:
            if num <= self.larger[0]:
                heappush(self.smaller, -1*num)
            else:
                heappush(self.smaller, -1*heappop(self.larger))
                heappush(self.larger, num)
        else:
            if num >= self.larger[0]:
                heappush(self.larger, num)
            else:
                heappush(self.smaller, -1*num)
            
            if len(self.smaller) > len(self.larger):
                heappush(self.larger, -1*heappop(self.smaller))
            
            if len(self.larger) > len(self.smaller) + 1:
                heappush(self.smaller, -1*heappop(self.larger))
                    
    def findMedian(self) -> float:
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return (self.larger[0] + -1*self.smaller[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []
        self.size = 0

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.storage, num)
        self.size += 1
        
    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return self.storage[self.size // 2]
        else:
            index = self.size // 2
            return (self.storage[index - 1] + self.storage[index]) / 2