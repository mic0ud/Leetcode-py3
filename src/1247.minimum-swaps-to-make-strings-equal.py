#
# @lc app=leetcode id=1247 lang=python3
#
# [1247] Minimum Swaps to Make Strings Equal
#
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
#
# algorithms
# Medium (58.81%)
# Likes:    210
# Dislikes: 123
# Total Accepted:    10.8K
# Total Submissions: 18.2K
# Testcase Example:  '"xx"\r\n"yy"\r'
#
# You are given two strings s1 and s2 of equal length consisting of letters "x"
# and "y" only. Your task is to make these two strings equal to each other. You
# can swap any two characters that belong to different strings, which means:
# swap s1[i] and s2[j].
# 
# Return the minimum number of swaps required to make s1 and s2 equal, or
# return -1 if it is impossible to do so.
 
# Example 1:
 
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: 
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
# 
# Example 2: 
 
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: 
# Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we
# can only swap chars in different strings.
# 
# Example 3:

# Input: s1 = "xx", s2 = "xy"
# Output: -1

# Example 4:

# Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# Output: 4

# Constraints:
 
# 1 <= s1.length, s2.length <= 1000
# s1, s2 only contain 'x' or 'y'.


# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                x_y += 1
            if s1[i] == 'y' and s2[i] == 'x':
                y_x += 1
        if (x_y + y_x) % 2 > 0:
            return -1
        res = x_y // 2 + y_x // 2 + x_y % 2 + y_x % 2
        return res
# @lc code=end

