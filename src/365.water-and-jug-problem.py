#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (29.69%)
# Likes:    235
# Dislikes: 659
# Total Accepted:    35.3K
# Total Submissions: 117.7K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities x and y litres. There is an infinite
# amount of water supply available. You need to determine whether it is
# possible to measure exactly z litres using these two jugs.
# 
# If z liters of water is measurable, you must have z liters of water contained
# within one or both buckets by the end.
# 
# Operations allowed:
# 
# 
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or
# the first jug itself is empty.
# 
# 
# Example 1: (From the famous "Die Hard" example)
# 
# 
# Input: x = 3, y = 5, z = 4
# Output: True
# 
# 
# Example 2:
# 
# 
# Input: x = 2, y = 6, z = 5
# Output: False


# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return False
        gcd = self.gcd(x, y)
        return z == 0 if gcd == 0 else z % gcd == 0
        
    def gcd(self, a, b) -> int:
        a, b = max(a,b), min(a,b)
        if b == 0:
            return a
        while True:
            if a % b == 0:
                return b
            a, b = b, a%b
# @lc code=end

