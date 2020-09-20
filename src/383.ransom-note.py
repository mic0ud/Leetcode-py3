#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.37%)
# Likes:    578
# Dislikes: 192
# Total Accepted:    214.2K
# Total Submissions: 404.6K
# Testcase Example:  '"a"\n"b"'
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# You may assume that both strings contain only lowercase letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr, cm = Counter(ransomNote), Counter(magazine)
        for k,v in cr.items():
            if v > cm[k]:
                return False
        return True
# @lc code=end

