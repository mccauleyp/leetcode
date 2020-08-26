'''
https://leetcode.com/problems/lru-cache/
146. LRU Cache
Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
# This solution uses an Ordered Dictionary, and the solution after that uses a regular 
# dictionary and a list to keep track of the key orders (much slower)
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if self.capacity == 0:
                self.cache.popitem(last=False)
            else:
                self.capacity -= 1
            self.cache[key] = value 
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.order = []
        self.capacity = capacity
        
    def move_to_front(self, key: int):
        index = self.order.index(key)
        self.order.append(self.order.pop(index))
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.move_to_front(key)
            return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.move_to_front(key)
        else:
            if self.capacity == 0:
                self.cache.pop(self.order.pop(0))
            else:
                self.capacity -= 1
            self.cache[key] = value
            self.order.append(key)
                        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)