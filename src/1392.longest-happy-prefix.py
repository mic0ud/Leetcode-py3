#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#
# https://leetcode.com/problems/longest-happy-prefix/description/
#
# algorithms
# Hard (39.14%)
# Likes:    191
# Dislikes: 15
# Total Accepted:    8K
# Total Submissions: 20.1K
# Testcase Example:  '"level"'
#
# A string is called a happy prefix if is a non-empty prefix which is also a
# suffix (excluding itself).
# 
# Given a string s. Return the longest happy prefix of s .
# 
# Return an empty string if no such prefix exists.
# 
# 
# Example 1:
# 
# 
# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
# suffix is given by "l".
# 
# 
# Example 2:
# 
# 
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can
# overlap in the original string.
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcodeleet"
# Output: "leet"
# 
# 
# Example 4:
# 
# 
# Input: s = "a"
# Output: ""
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        sp = self.suffix_prefix(s)
        return s[:sp[-1]]

    def suffix_prefix(self, s) -> [int]:
        res, i = [0], 0
        for j in range(1, len(s)):
            while i > 0 and s[i] != s[j]:
                i = res[i-1]
            if s[i] == s[j]:
                res.append(i+1)
                i += 1
            else:
                res.append(0)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestPrefix("levele")
    s.longestPrefix("leetcodeleet")
