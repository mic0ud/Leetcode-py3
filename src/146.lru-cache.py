#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (28.44%)
# Likes:    4154
# Dislikes: 172
# Total Accepted:    400.8K
# Total Submissions: 1.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
class LRUCache_:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.visit = {}
        self.visitCount = {}
        self.count = 1

    def get(self, key: int) -> int:
        if key not in self.data.keys():
            return -1
        else:
            oldCount = self.visit[key]
            self.visit[key] = self.count
            self.count += 1
            self.visitCount.pop(oldCount, None)
            self.visitCount[self.visit[key]] = key
            return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            oldCount = self.visit[key]
            self.visit[key] = self.count
            self.count += 1
            self.visitCount.pop(oldCount, None)
            self.visitCount[self.visit[key]] = key
        else:
            if len(self.data) == self.capacity:
                minCount = min(self.visitCount.keys())
                lru = self.visitCount[minCount]
                self.visitCount.pop(minCount, None)
                self.data.pop(lru, None)
            self.visit[key] = self.count
            self.count += 1
            self.visitCount[self.visit[key]] = key
        self.data[key] = value


class LRUCache:
    def __init__(self, capacity: int):
        self.count = 1
        self.data = dict()
        self.key_timestamp = dict()
        self.timestamp_key = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        res = self.data[key] if key in self.data else -1
        if res != -1:
            self.timestamp_key.pop(self.key_timestamp[key])
            self.key_timestamp[key] = self.count
            self.timestamp_key[self.count] = key
            self.count += 1
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.data) == self.cap:
                least = min(self.timestamp_key.keys()) 
                least_key = self.timestamp_key[least]
                self.timestamp_key.pop(least)
                self.data.pop(least_key)
                self.key_timestamp.pop(least_key)                    
        else:
            self.timestamp_key.pop(self.key_timestamp[key])            
        self.key_timestamp[key] = self.count
        self.timestamp_key[self.count] = key
        self.data[key] = value
        self.count += 1            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == '__main__':
    s = LRUCache(2)
    s.put(2,1)
    s.put(1,1)
    s.put(2,3)
    s.put(4,1)
    s.get(1)
    s.get(2)

    # s.put(1,1)
    # s.put(2,2)
    # s.get(1)
    # s.put(3,3)
    # s.get(2)
    # s.put(4,4)
    # s.get(1)
    # s.get(3)
    # s.get(4)