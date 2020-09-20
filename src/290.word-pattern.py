#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.53%)
# Likes:    1014
# Dislikes: 144
# Total Accepted:    182.2K
# Total Submissions: 497.3K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        str_list = str1.split(' ')
        if len(pattern) != len(str_list):
            return False
        m1, m2 = defaultdict(str), defaultdict(str)
        for i,p in enumerate(pattern):
            if p not in m1 and str_list[i] not in m2:
                m1[p] = str_list[i]
                m2[str_list[i]] = p
            else:
                if m1[p] != str_list[i] or m2[str_list[i]] != p:
                    return False
        return True
# @lc code=end

