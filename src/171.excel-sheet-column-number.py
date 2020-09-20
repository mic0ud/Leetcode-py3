#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (52.70%)
# Likes:    704
# Dislikes: 130
# Total Accepted:    251.9K
# Total Submissions: 476.5K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        res = ord(s[-1]) - 64
        for i in range(len(s)-1):
            res += (ord(s[i]) - 64) * (26 ** (len(s)-1-i))
        return res
# @lc code=end

