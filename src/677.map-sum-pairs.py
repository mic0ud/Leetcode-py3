#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (52.42%)
# Likes:    397
# Dislikes: 70
# Total Accepted:    34.4K
# Total Submissions: 65.2K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'

# Implement a MapSum class with insert, and sum methods.

# For the method insert, you'll be given a pair of (string, integer). The
# string represents the key and the integer represents the value. If the key
# already existed, then the original key-value pair will be overridden to the
# new one.
 
# For the method sum, you'll be given a string representing the prefix, and you
# need to return the sum of all the pairs' value whose key starts with the
# prefix.
# 
# 
# Example 1:
# 
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

# @lc code=start
from collections import defaultdict
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # root = {'a': [0, {}], 'p': [0, {}]}
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        r = self.root
        for i, c in enumerate(key):
            if c not in r:
                r[c] = [0, {}]
            if i == len(key)-1:
                r[c][0] = val
            else:
                r = r[c][1]

    def sum(self, prefix: str) -> int:
        r, res = self.root, [0]
        for i, c in enumerate(prefix):
            if c in r:
                if i == len(prefix)-1:
                    res[0] += r[c][0]
                r = r[c][1]
            else:
                return 0            
        self.sum_helper(r, res)
        return res[0]        
    
    def sum_helper(self, r, res: [int]):
        if not r:
            return
        for v in r.values():
            res[0] += v[0]
            self.sum_helper(v[1], res)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end
if __name__ == '__main__':
    s = MapSum()
    s.insert("apple", 3)
    s.sum("apple")
    s.insert("app", 2)
    s.sum("ap")
