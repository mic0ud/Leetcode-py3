#
# @lc app=leetcode id=1124 lang=python3
#
# [1124] Longest Well-Performing Interval
#
# https://leetcode.com/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (31.87%)
# Likes:    269
# Dislikes: 47
# Total Accepted:    8.1K
# Total Submissions: 25.2K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# We are given hours, a list of the number of hours worked per day for a given
# employee.
# 
# A day is considered to be a tiring day if and only if the number of hours
# worked is (strictly) greater than 8.
# 
# A well-performing interval is an interval of days for which the number of
# tiring days is strictly larger than the number of non-tiring days.
# 
# Return the length of the longest well-performing interval.
# 
# 
# Example 1:
# 
# 
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16
# 
# 
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: [int]) -> int:
        if not hours:
            return 0
        score = 0 # tiring day +1, normal day -1
        lastScore = {}
        res = 0
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1 # !!!
            lastScore.setdefault(score, i)
            if score-1 in lastScore: # score -[score-1] == 1 > 0, valid
                res = max(res, i-lastScore[score-1])
        return res
# @lc code=end
# [6,9,9]
if __name__ == '__main__':
    s = Solution()
    s.longestWPI([6,9,9])
