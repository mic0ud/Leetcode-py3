#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (66.29%)
# Likes:    804
# Dislikes: 81
# Total Accepted:    171.5K
# Total Submissions: 254.9K
# Testcase Example:  '"Let\'s take LeetCode contest"'
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([ss[::-1] for ss in s.split(' ')])
# @lc code=end

