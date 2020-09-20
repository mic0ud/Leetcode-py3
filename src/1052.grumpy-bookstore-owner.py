#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#
# https://leetcode.com/problems/grumpy-bookstore-owner/description/
#
# algorithms
# Medium (53.28%)
# Likes:    242
# Dislikes: 20
# Total Accepted:    15.5K
# Total Submissions: 28.6K
# Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
#
# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and
# all those customers leave after the end of that minute.
# 
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
# bookstore owner is grumpy, the customers of that minute are not satisfied,
# otherwise they are satisfied.
# 
# The bookstore owner knows a secret technique to keep themselves not grumpy
# for X minutes straight, but can only use it once.
# 
# Return the maximum number of customers that can be satisfied throughout the
# day.

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3
# minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5
# = 16.

# Note:
# 
# 
# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: [int], grumpy: [int], X: int) -> int:
        if not customers:
            return 0
        if not grumpy or X >= len(customers):
            return sum(customers)
        sumX, sumNormal = sum(customers[:X]), sum([customers[i] for i in range(X,len(customers)) if grumpy[i] == 0])
        res = sumX + sumNormal
        for i in range(1, len(customers)-X+1):
            sumX += customers[i+X-1] - customers[i-1]
            sumNormal += (0 if grumpy[i-1]==1 else customers[i-1]) - (0 if grumpy[i+X-1]==1 else customers[i+X-1])
            res = max(res, sumX+sumNormal)
        return res
# @lc code=end

