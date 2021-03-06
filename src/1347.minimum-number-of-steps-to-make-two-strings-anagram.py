#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
#
# algorithms
# Medium (75.13%)
# Likes:    174
# Dislikes: 15
# Total Accepted:    20.1K
# Total Submissions: 26.9K
# Testcase Example:  '"bab"\n"aba"'
#
# Given two equal-size strings s and t. In one step you can choose any
# character of t and replace it with another character.
# 
# Return the minimum number of steps to make t an anagram of s.
# 
# An Anagram of a string is a string that contains the same characters with a
# different (or the same) ordering.
# 
# 
# Example 1:
# 
# 
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of
# s.
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters
# to make t anagram of s.
# 
# 
# Example 3:
# 
# 
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
# 
# 
# Example 4:
# 
# 
# Input: s = "xxyyzz", t = "xxyyzz"
# Output: 0
# 
# 
# Example 5:
# 
# 
# Input: s = "friend", t = "family"
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 50000
# s.length == t.length
# s and t contain lower-case English letters only.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for c in s:
            t = t.replace(c,'',1)
        return len(t)

    def minSteps_(self, s: str, t: str) -> int:
        sc, tc = Counter(s), Counter(t)
        tmp = sc - tc
        res = sum(tmp.values())
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minSteps("bab", "aba")
    s.minSteps("leetcode", "practice")
