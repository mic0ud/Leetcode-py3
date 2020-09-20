#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (51.88%)
# Likes:    493
# Dislikes: 65
# Total Accepted:    43.9K
# Total Submissions: 84.9K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
#  '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Create a timebased key-value store class TimeMap, that supports two
# operations.
# 
# 1. set(string key, string value, int timestamp)
# 
# 
# Stores the key and value, along with the given timestamp.
# 
# 
# 2. get(string key, int timestamp)
# 
# 
# Returns a value such that set(key, value, timestamp_prev) was called
# previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest
# timestamp_prev.
# If there are no values, it returns the empty string ("").

# Example 1:
# 
# 
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs =
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:   
# TimeMap kv;   
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with
# timestamp = 1   
# kv.get("foo", 1);  // output "bar"   
# kv.get("foo", 3); // output "bar" since there is no value corresponding to
# foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie
# "bar"   
# kv.set("foo", "bar2", 4);   
# kv.get("foo", 4); // output "bar2"   
# kv.get("foo", 5); //output "bar2"   

# Example 2:
# 
# 
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs
# =
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]

# Note:
# 
# 
# All key/value strings are lowercase.
# All key/value strings have length in the range [1, 100]
# The timestamps for all TimeMap.set operations are strictly increasing.
# 1 <= timestamp <= 10^7
# TimeMap.set and TimeMap.get functions will be called a total of 120000 times
# (combined) per test case.
# 
# 
#

# @lc code=start
from collections import defaultdict
from bisect import bisect_left
# class TimeMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         # {'key': {1: 'val1', 2:'val2'}}
#         self.data = defaultdict(dict)
#         self.keys = defaultdict(list)
#         # {'key': [(1, 'val1'), (2,'val2')]}
#         #self.data = defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.data:
#             self.data[key] = defaultdict(str)
#         self.data[key][timestamp] = value
#         self.keys[key].append(timestamp)

#     def get(self, key: str, timestamp: int) -> str:
#         if timestamp in self.keys[key]:
#             return self.data[key][timestamp]
#         p = bisect_left(self.keys[key], timestamp)
#         return self.data[key][self.keys[key][p-1]] if p > 0 else ''

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # {'key': [(1, 'val1'), (2,'val2')]}
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        idx = bisect_left(self.data[key], (timestamp,'{')) # '{' is larger than 'z', '(' is less than 'A'
        return self.data[key][idx-1][1] if idx > 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# [null,null,null,"","high","low","low","low"]
# [null,null,null,"","high","high","low","low"]
# ["TimeMap","set","set","get","get","get","get","get"]\n[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
if __name__ == '__main__':
    s = TimeMap()
    s.set("love","high",10)
    s.set("love","low",20)
    s.get("love",15)
