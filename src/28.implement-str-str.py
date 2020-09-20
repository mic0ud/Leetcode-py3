#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.25%)
# Likes:    1412
# Dislikes: 1772
# Total Accepted:    622.4K
# Total Submissions: 1.8M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        res = self.search(haystack, needle)
        return -1 if not res else res[0]

    def search(self, haystack, needle) -> [int]:
        res, i, j = [], 0, 0
        sp = self.suffix_prefix(needle)
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    res.append(i-j)
                    j = sp[j-1]
            else:
                if j == 0:
                    i += 1
                else:
                    j = sp[j-1]
        return res

    def suffix_prefix(self, needle: str) -> [int]:
        res, i = [0], 0
        for j in range(1, len(needle)):
            while needle[j] != needle[i] and i > 0:
                i = res[i-1]
            if needle[j] == needle[i]:
                res.append(i+1)
                i += 1
            else:
                res.append(0)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.strStr('helloworld', 'll')
