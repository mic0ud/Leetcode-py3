#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (56.85%)
# Likes:    224
# Dislikes: 57
# Total Accepted:    37.5K
# Total Submissions: 64.8K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
# 
# 
# 
# Example:
# 
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
# 
# 
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # total operation is 10000 including 3 types of operation, so the total distinct keys is about 3000
        self.arr = [[] for _ in range(2500)]

    def add(self, key: int) -> None:
        idx = key % 2500
        if key not in self.arr[idx]:
            self.arr[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % 2500
        if key in self.arr[idx]:
            self.arr[idx].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % 2500
        return key in self.arr[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

