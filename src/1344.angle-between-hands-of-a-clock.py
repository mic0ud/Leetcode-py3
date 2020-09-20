#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#
# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/
#
# algorithms
# Medium (60.69%)
# Likes:    120
# Dislikes: 31
# Total Accepted:    9.3K
# Total Submissions: 15.4K
# Testcase Example:  '12\n30'
#
# Given two numbers, hour and minutes. Return the smaller angle (in degrees)
# formed between the hour and the minute hand.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: hour = 12, minutes = 30
# Output: 165
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: hour = 3, minutes = 30
# Output: 75
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: hour = 3, minutes = 15
# Output: 7.5
# 
# 
# Example 4:
# 
# 
# Input: hour = 4, minutes = 50
# Output: 155
# 
# 
# Example 5:
# 
# 
# Input: hour = 12, minutes = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.
# 
# 
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        h = hour*30+30*(minutes/60)
        m = minutes*6
        res = abs(h-m)
        return min(res, 360-res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.angleClock(4,50)
    s.angleClock(12,0)
    s.angleClock(3,15)
    s.angleClock(3,30)
    s.angleClock(12,30)
