#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (47.08%)
# Likes:    461
# Dislikes: 206
# Total Accepted:    58.6K
# Total Submissions: 123.1K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"

# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"

# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


# @lc code=start
class Solution:
    def findLongestWord(self, s, d):
        for word in sorted(d, key = lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word): return word
        return ''
        
    def findLongestWord_SLOW(self, s: str, d: [str]) -> str:
        res = ''
        for ds in d:
            if self.check(s, ds):
                if len(ds) > len(res) or (len(ds) == len(res) and ds < res):
                    res = ds
        return res

    def check(self, s, d) -> bool:
        if s == d:
            return True
        if len(s) < len(d):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(d):
            while i < len(s) and s[i] != d[j]:
                i += 1
            if i >= len(s):
                return False
            i += 1
            j += 1
        return j == len(d)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
