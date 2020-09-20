#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (39.23%)
# Likes:    2031
# Dislikes: 151
# Total Accepted:    165.9K
# Total Submissions: 419.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        if not s or not p or len(p) > len(s):
            return []
        countP = defaultdict(int)
        for c in p:
            countP[c] += 1
        res = []
        countWindow = defaultdict(int)
        for i in range(len(p)):
            countWindow[s[i]] += 1
        if countP == countWindow:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            countWindow[s[i-1]] -= 1
            if countWindow[s[i-1]] == 0:
                countWindow.pop(s[i-1], None)
            countWindow[s[len(p)+i-1]] += 1
            if countP == countWindow:
                res.append(i)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findAnagrams("cbaebabacd", 'abc')
