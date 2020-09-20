#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/
#
# algorithms
# Medium (44.19%)
# Likes:    247
# Dislikes: 15
# Total Accepted:    10.4K
# Total Submissions: 23K
# Testcase Example:  '"croakcroak"'
#
# Given the string croakOfFrogs, which represents a combination of the string
# "croak" from different frogs, that is, multiple frogs can croak at the same
# time, so multiple “croak” are mixed. Return the minimum number of different
# frogs to finish all the croak in the given string.
# 
# A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’
# sequentially. The frogs have to print all five letters to finish a croak. If
# the given string is not a combination of valid "croak" return -1.
# 
# 
# Example 1:
# 
# 
# Input: croakOfFrogs = "croakcroak"
# Output: 1 
# Explanation: One frog yelling "croak" twice.
# 
# 
# Example 2:
# 
# 
# Input: croakOfFrogs = "crcoakroak"
# Output: 2 
# Explanation: The minimum number of frogs is two. 
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
# 
# 
# Example 3:
# 
# 
# Input: croakOfFrogs = "croakcrook"
# Output: -1
# Explanation: The given string is an invalid combination of "croak" from
# different frogs.
# 
# 
# Example 4:
# 
# 
# Input: croakOfFrogs = "croakcroa"
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= croakOfFrogs.length <= 10^5
# All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 > 0:
            return -1
        res, counter = 0, defaultdict(deque)
        for i,cr in enumerate(croakOfFrogs):
            counter[cr].append(i)
            if cr != 'c':
                res = max(res, len(counter['c']))
            if all(len(counter[cc]) > 0 for cc in 'croak'):
                c,r,o,a,k = counter['c'].popleft(),counter['r'].popleft(),counter['o'].popleft(),counter['a'].popleft(),counter['k'].popleft()
                if not c<r<o<a<k:
                    return -1
        if any(len(counter[cc]) > 0 for cc in 'croak'):
            return -1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minNumberOfFrogs("crocakcroraoakk")
    s.minNumberOfFrogs("aoocrrackk")
    s.minNumberOfFrogs("croakcroak")
    s.minNumberOfFrogs("crcoakroak")
