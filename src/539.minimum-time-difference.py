#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (49.74%)
# Likes:    378
# Dislikes: 129
# Total Accepted:    42.8K
# Total Submissions: 84.6K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1

# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: [str]) -> int:
        n = len(timePoints)
        if n < 2:
            return 0
        converted = sorted([self.convert(t) for t in timePoints])
        res = float('inf')
        for i in range(1, n):
            res = min(res, converted[i]-converted[i-1])
            if i == n-1:
                res = min(res, 24*60-(converted[i]-converted[0]))
        return res

    def convert(self, t) -> int:
        h, m = t.split(':')
        return int(h)*60 + int(m)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findMinDifference(["22:59","00:01", '01:59'])