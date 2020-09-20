#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (57.85%)
# Likes:    916
# Dislikes: 84
# Total Accepted:    117.6K
# Total Submissions: 202.9K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        countMap = {}
        for c in s:
            if c in countMap.keys():
                countMap[c] += 1
            else:
                countMap[c] = 1

        frqMap = {}
        for k, v in countMap.items():
            if v in frqMap.keys():
                frqMap[v].append(k)
            else:
                frqMap[v] = [k]
        res = ''
        for kk in sorted(frqMap.keys()):
            for vv in frqMap[kk]:
                ss = vv * kk
                res = ss + res
        return res
# @lc code=end

