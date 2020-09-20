#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (46.56%)
# Likes:    334
# Dislikes: 50
# Total Accepted:    22.4K
# Total Submissions: 47.4K
# Testcase Example:  '["un","iq","ue"]'
#
# Given an array of strings arr. String s is a concatenation of a sub-sequence
# of arr which have unique characters.
# 
# Return the maximum possible length of s.
# 
# 
# Example 1:
# 
# 
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and
# "ique".
# Maximum length is 4.
# 
# 
# Example 2:
# 
# 
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# 
# 
# Example 3:
# 
# 
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.
# 
# 
#

# @lc code=start
class Solution:
    def maxLength(self, arr: [str]) -> int:
        dp = [set()]
        for a in arr:
            if len(a) == len(set(a)):
                a = set(a)
                for d in dp:
                    if not d & a:
                        dp.append(d|a)
        return max(len(d) for d in dp)

    def maxLength_SLOW(self, arr: [str]) -> int:
        res = [0]
        def search(i, path: str):
            if i >= len(arr):
                if len(path) == len(set(path)):
                    res[0] = max(res[0], len(path))
                return
            search(i+1, path)
            search(i+1, path+arr[i])
        search(0,'')
        return res[0]
# @lc code=end

