#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (50.00%)
# Likes:    666
# Dislikes: 59
# Total Accepted:    44.8K
# Total Submissions: 89.2K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
# 
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
# 
# 
# 
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion. 
# 
# 
# 
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
# 
# 
# 
# Example 1:
# 
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# 
# 
# 
# Note:
# 
# The number of given pairs will be in the range [1, 1000].
# 
# 
#

# @lc code=start
from operator import itemgetter
class Solution:
    def findLongestChain(self, pairs: [[int]]) -> int:
        if not pairs or not pairs[0]:
            return 0
        pairs = sorted(pairs, key=itemgetter(1))
        count = 1
        end = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                count += 1
                end = pairs[i][1]
        return count
# @lc code=end

