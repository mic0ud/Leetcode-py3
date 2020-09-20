#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (61.18%)
# Likes:    1819
# Dislikes: 56
# Total Accepted:    105.5K
# Total Submissions: 171.9K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for t in range(len(T))]
        for i in range(len(T)):
            while stack and T[i] > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = i - item[0]
            stack.append((i, T[i]))
        return res
# @lc code=end

